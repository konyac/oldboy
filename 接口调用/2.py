#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests,json

def main():
    # 配置您申请的APPKey
    appkey = "790bd7c4dcfe7e4e223a9d3965664dbd"

    # 1.手机归属地查询
    request1(appkey, "GET")


# 手机归属地查询
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/mobile/get"
    params = {
        "phone": "15225092013",  # 需要查询的手机号码或手机号码前7位
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }

    f = requests.get(url, params=params)

    content = f.text
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