#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import xlrd, xlwt, os
import threading, time

fname = "hangye.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print("no sheet in %s named Sheet1" % fname)
# 获取行数
nrows = sh.nrows
# 获取列数
ncols = sh.ncols
# print("nrows %d, ncols %d" % (nrows, ncols))
# 获取第一行第一列数据
print(nrows, ncols)
# cell_value = sh.cell_value(0, 7)  # 获取11列的

dict = {"work_list": []}


for item in range(0, nrows):
    tmepdict = {}
    er_dict = {}
    key = sh.cell_value(item, 0)  # 获取11列的
    tmepdict["categoryname"] = key
    tmepdict["id"] = item + 1
    tmepdict["work_list"] = []
    for start in range(1, ncols):
        value = sh.cell_value(item, start)
        if not value:
            continue
        id = str(item + 1) + "0" + str(start)
        print(id)
        er_dict = {"categoryname": value, "id": id}
        tmepdict["work_list"].append(er_dict)
        # print(key, "======", value)
        # print(tempdict)
    dict['work_list'].append(tmepdict)
print(dict)
