#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
#coding:utf-8
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
glod=int(input("您的总资产为："))
def show_goods():
    for i in goods:
        print(str(goods.index(i)) + ":" + i["name"], i["price"], "元")
    print("4:结算")
def show_gwc():
    for item in gwc.items():
        print(item[0], "数量：" + str(item[1]["数量"]), "单价：" + str(item[1]["单价"]))
total=0
gwc={}
show_goods()
while True:
    get_goods=int(input("请输入你要购买的商品编号,结算请输入4："))
    if get_goods<3:
        if goods[get_goods]["name"] in gwc.keys():
            gwc[goods[get_goods]["name"]]["数量"]+=1
        else:
            gwc[goods[get_goods]["name"]] = {"数量": 1, "单价": goods[get_goods]["price"]}
        total = total + goods[get_goods]["price"]
        show_gwc()
        show_goods()
        continue
    # if get_goods==0:
    #     #gwc.append(goods[get_goods]["name"])
    #     a += 1
    #     gwc[goods[get_goods]["name"]]={"数量":a,"单价":goods[get_goods]["price"]}
    #     total=total+goods[get_goods]["price"]
    #     show_gwc()
    #     show_goods()
    #     continue
    # elif get_goods==1:
    #     #gwc.append(goods[get_goods]["name"])
    #     b += 1
    #     gwc[goods[get_goods]["name"]]={"数量":b,"单价":goods[get_goods]["price"]}
    #     total=total+goods[get_goods]["price"]
    #     show_gwc()
    #     show_goods()
    #     continue
    # elif get_goods==2:
    #     #gwc.append(goods[get_goods]["name"])
    #     c += 1
    #     gwc[goods[get_goods]["name"]]={"数量":c,"单价":goods[get_goods]["price"]}
    #     total=total+goods[get_goods]["price"]
    #     show_gwc()
    #     show_goods()
    #     continue
    # elif get_goods==3:
    #     #gwc.append(goods[get_goods]["name"])
    #     d += 1
    #     gwc[goods[get_goods]["name"]]={"数量":d,"单价":goods[get_goods]["price"]}
    #     total=total+goods[get_goods]["price"]
    #     show_gwc()
    #     show_goods()
    #     continue
    elif get_goods>4:
        print("输入错误")
        show_goods()
        continue
    else:
        if total<=glod:
            print("你购买的商品总额为%d元,购买成功" % total)
        else:
            print("余额不足")
        break





