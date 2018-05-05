#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os, json, copy, datetime, collections
from JF.backend.core import request_handler
from JF.models import jifen_orm as ORM
from JF.backend.utils.pager import Pagination
from JF.backend.utils import decrator
from JF.backend.utils.response import BaseResponse, StatusCodeEnum
from sqlalchemy import and_, or_
from JF.backend import commons
from JF.forms.home import IndexForm


class IndexHandler(request_handler.BaseRequestHandler):
    @decrator.auth_login_redirect
    def get(self, page=1):
        conn = ORM.session()
        current_user_id = self.session['user_info']['nid'] if self.session['is_login'] else 0
        current_user = self.session['user_info']['name']
        # print(current_user_id,current_user)

        # all_count = conn.query(ORM.News).count()
        #
        # obj = Pagination(page, all_count)
        #
        #
        result = conn.query(
            ORM.Item.name,
            ORM.zhibiao.Zname,
            ORM.Upload.content,
            ORM.Upload.value,
            ORM.Upload.ctime,
            ORM.Upload.status,
        ).join(ORM.Upload, isouter=True).join(ORM.zhibiao, isouter=True).filter(
            ORM.Upload.user_id == current_user_id).order_by(ORM.Upload.ctime.desc()).all()

        item_fl = conn.query(ORM.Fenlei.fname).all()
        item_info = conn.query(ORM.Item.name, ORM.Erji.Ename, ORM.Fenlei.fname).join(ORM.Erji, isouter=True).join(
            ORM.Fenlei, isouter=True).all()
        item_ej = conn.query(ORM.Erji.Ename).all()
        extra_info = conn.query(ORM.zhibiao.Zname, ORM.Item.name).join(ORM.Item, isouter=True).all()
        conn.close()
        #
        # str_page = obj.string_pager('/index/')
        # print(result)

        self.render('home/manager.html', uploaded=result, username=current_user, item_fl=item_fl,item_info=item_info,item_ej=item_ej,extra_info=extra_info )

    @decrator.auth_login_json
    def post(self, *args, **kwargs):
        rep = BaseResponse()

        form = IndexForm()
        if form.valid(self):
            # title,content,href,news_type,user_info_id

            input_dict = copy.deepcopy(form._value_dict)
            input_dict['ctime'] = datetime.datetime.now()
            input_dict['user_info_id'] = self.session['user_info']['nid']
            conn = ORM.session()
            conn.add(ORM.News(**input_dict))
            conn.commit()
            conn.close()
            rep.status = True
        else:
            rep.message = form._error_dict

        self.write(json.dumps(rep.__dict__))


class UploadImageHandler(request_handler.BaseRequestHandler):
    @decrator.auth_login_json
    def post(self, *args, **kwargs):
        rep = BaseResponse()
        try:
            file_metas = self.request.files["img"]
            for meta in file_metas:
                file_name = meta['filename']
                file_path = os.path.join('statics', 'upload', commons.generate_md5(file_name))
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
            rep.status = True
            rep.data = file_path
        except Exception as ex:
            rep.summary = str(ex)
        self.write(json.dumps(rep.__dict__))


class UserInfoHandler(request_handler.BaseRequestHandler):  # 继承类RequestHandler
    @decrator.auth_login_redirect
    def get(self, *args, **kwargs):
        conn = ORM.session()
        current_user_id = self.session['user_info']['nid'] if self.session['is_login'] else 0
        user_info = conn.query(ORM.UserInfo.name,
                               ORM.UserInfo.sex,
                               ORM.UserInfo.birth,
                               ORM.UserInfo.inout,
                               ORM.Position_fl.name,
                               ORM.Position.name,
                               ORM.Department.name).join(ORM.Department, isouter=True).join(ORM.Position,
                                                                                            isouter=True).join(
            ORM.Position_fl,
            isouter=True).filter(
            ORM.UserInfo.nid == current_user_id).first()
        department_info = conn.query(ORM.Department.name, ).all()
        position_info = conn.query(ORM.Position.name, ORM.Position.inout, ORM.Position_fl.name).join(ORM.Position_fl,
                                                                                                     isouter=True).order_by(
            ORM.Position.nid.asc()).all()
        position_info_fl = conn.query(ORM.Position_fl.name).all()
        conn.close()
        self.render("home/userinfo.html", user_info=user_info, department_info=department_info,
                    position_info=position_info, position_info_fl=position_info_fl)

    def post(self, *args, **kwargs):
        pass
