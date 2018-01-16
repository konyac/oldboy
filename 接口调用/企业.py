#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests, json
#https://way.jd.com/qichacha/GetBriefIntroduction?key=736be44d18e011e6b4fb1051721d3b62&companyName=小米科技有限责任公司&dtype=json&appkey=6831311b16156e8775fff0364cb69d67
import re
def main():
    # 配置您申请的APPKey
    appkey = "6831311b16156e8775fff0364cb69d67"
    company = input('公司名：')

    # 1.手机归属地查询
    request1(appkey, company)


# 手机归属地查询
def request1(appkey, com):
    # url = "https://way.jd.com/jindidata/detail_info"
    url = "https://way.jd.com/qichacha/GetBriefIntroduction"
    params = {
        'key':'736be44d18e011e6b4fb1051721d3b62',
        # "name": com,
        "companyName": com,
        "appkey": appkey,  # 应用APPKEY(应用详细页查询)
        # 'dtype':'json',
        # 'key':'736be44d18e011e6b4fb1051721d3b62'
    }

    f = requests.get(url, params=params)

    content = f.text
    res = json.loads(content)
    print(res)
    if res:
        error_code = res["code"]
        print(error_code)
        if error_code == '10000':
            # 成功请求
            # print(res["result"]['result']['baseInfo']['businessScope'],)、
            ret = res["result"]['Result'].get('Content',None)
            ret = re.sub('^<*>$','',ret)
            print(ret)
        else:
            print("%s:%s" % (res["code"], res["msg"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()
