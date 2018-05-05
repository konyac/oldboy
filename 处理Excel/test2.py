#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import xlrd, xlwt, os
import threading ,time

fname = "低值易耗资产明细.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("资产列表")
except:
    print("no sheet in %s named Sheet1" % fname)
# 获取行数
nrows = sh.nrows
# 获取列数
ncols = sh.ncols
# print("nrows %d, ncols %d" % (nrows, ncols))
# 获取第一行第一列数据
# cell_value = sh.cell_value(2, 10) #获取11列的
# print (cell_value)
base_path = os.path.dirname(__file__)


row_list = []
# 获取各行数据
for i in range(2, nrows):  # 从第三行开始
    cell_value_now = sh.cell_value(i, 10)
    cell_value_before = sh.cell_value(i - 1, 10)
    if cell_value_before == cell_value_now:
        row_data = sh.row_values(i)
        row_list.append(row_data)
    else:
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet
        head = 0
        for each_row in row_list:
            for k in range(0, len(each_row)):
                sheet1.write(head, k, each_row[k])
            head += 1
            path = os.path.join(base_path, 'statics', str(cell_value_before) + '.xls')
            print(path)
            f.save(path)
        row_list = []
