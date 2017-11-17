#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from newchouti.backend.form import fields


class BaseForm:
    '''
    基类
    '''
    def __init__(self):
        """
        封装最终的检测结果，和每个检测的结果和错误信息
        """
        self._value_dict = {}
        self._error_dict = {}
        self._valid_status = True
    def valid(self,handler):#handler 创建对象时传入的self。

        for field_name, field_obj in self.__dict__.items(): #循环每个验证类
            if field_name.startswith('_'):#去掉不是验证类的哪些字段，
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
            #以上代码，循环验证类。拿到要验证的数据。
            #以下执行验证
            # print(post_value)
            field_obj.match(field_name, post_value)#######执行验证。改变#########
            if field_obj.is_valid:
                self._value_dict[field_name] = field_obj.value
            else:
                self._error_dict[field_name] = field_obj.error
                self._valid_status = False #初始是正确的有一个验证错误，就改为了False
        return self._valid_status
