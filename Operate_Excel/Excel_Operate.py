import xlrd
date = xlrd.open_workbook('test.xlsx')
table = date.sheets()[0]    #打开第一张表
nrows = table.nrows
for i in range():
    if i == 0:
        continue
    print table.row_values(i)[:13]  #取前13列
