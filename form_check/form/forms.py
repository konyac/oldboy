#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from form_check.form import fields


class BaseForm:
    def __init__(self):
        self._value_dict = {}
        self._error_dict = {}
        self._valid_status = True
    def valid(self,handler):#handler 创建对象时传入的self。

        for field_name, field_obj in self.__dict__.items():
            if field_name.startswith('_'):#去掉不是类的哪些字段，
                continue
            if type(field_obj) == fields.CheckBoxField:#checkbox
                post_value = handler.get_arguments(field_name, None)
            elif type(field_obj) == fields.FileField:#File
                post_value = []
                file_list = handler.request.files.get(field_name, [])
                for file_item in file_list:
                    post_value.append(file_item['filename'])
            else:
                post_value = handler.get_argument(field_name, None)#获取前端数据。

            field_obj.match(field_name, post_value)#执行验证。改变
            if field_obj.is_valid:
                self._value_dict[field_name] = field_obj.value
            else:
                self._error_dict[field_name] = field_obj.error
                self._valid_status = False
        return self._valid_status
