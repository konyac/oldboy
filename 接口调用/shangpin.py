#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json, urllib
from urllib.parse import urlencode
from urllib import request


# ----------------------------------
# 手机号码归属地调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/11
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = ""

    # 1.手机归属地查询
    request1(appkey, "GET")


# 手机归属地查询
def request1(appkey, m="GET"):
    url = "http://alibaba.wholesale.category.get"
    params = {
        "phone": "18530983738",  # 需要查询的手机号码或手机号码前7位
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = request.urlopen("%s" % (url))
    else:
        f = request.urlopen(url, params)

    content = f.read()
    content = str(content, encoding='utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
