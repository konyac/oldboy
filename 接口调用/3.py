#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests, json


def main():
    # 配置您申请的APPKey
    appkey = "4215cd6c6616ad2abe2ece9d23fe0fb3"
    company = input('公司名：')

    # 1.手机归属地查询
    request1(appkey, company)


# 手机归属地查询
def request1(appkey, com):
    url = "http://api.shenjian.io"
    params = {
        "companyName": com,
        "appid": appkey,  # 应用APPKEY(应用详细页查询)
    }

    f = requests.get(url, params=params)

    content = f.text
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["data"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
