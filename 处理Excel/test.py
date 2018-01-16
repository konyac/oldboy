#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import xlrd, xlwt,os

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
print("nrows %d, ncols %d" % (nrows, ncols))
# 获取第一行第一列数据
cell_value = sh.cell_value(1, 11) #获取11列的
# print cell_value

row_list = []
# 获取各行数据
start = 2
for i in range(1, nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)
count, y = divmod(len(row_list), 40)
start = 2
for i in range(count + 1):
    list = row_list[start:start + 40]
    start = start + 40
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet
    head = 0
    for each_row in list:
        for k in range(0, len(each_row)):
            sheet1.write(head, k, each_row[k])
        head += 1
    path =os.path.join(os.path.dirname(__file__),'static',str(i)+'.xls')
    print(path)
    f.save(path)