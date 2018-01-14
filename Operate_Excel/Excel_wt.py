#该脚本用来读取目标Excel中的内容

import xlwt
import xlrd
#读原始数据（所有的全局变量及数据源）
date_ori = xlrd.open_workbook('Ori_data.xlsx')
table_ori = date_ori.sheets()[0]    #打开第一张表
nrows_ori = table_ori.nrows
print (nrows_ori)

#读采集项（所需的全局变量）
data_need = xlrd.open_workbook('Collect.xlsx')
table_need = data_need.sheets()[0]    #打开第一张表
nrows_need = table_need.nrows
print (nrows_need)

#开始写数据
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')

for i in range (nrows_need):
    current_value_need = table_need.cell(i,0).value
    for j in range (nrows_ori):
        current_value_ori = table_ori.cell(j,1).value
        if (current_value_need == current_value_ori):
            worksheet.write(i,0,label = table_ori.cell(j,0).value)
            worksheet.write(i,1,label = table_ori.cell(j,1).value)
            continue
workbook.save('Excel_Workbook.xls')
