#encoding:utf8  
import xlrd  
import xlwt


data_origin = xlrd.open_workbook('origin.xls',w)
sheet_origin = data_origin.sheet_by_name(u'Sheet1')
rows_o = sheet_origin.nrows
cols_o = sheet_origin.ncols

data_chose = xlrd.open_workbook('chose.xls')
sheet_chose = data_chose.sheet_by_name(u'Sheet1')
rows_c = sheet_chose.nrows
cols_c = sheet_chose.ncols

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')


#打印origin的行跟列
#print (sheet_origin.nrows,sheet_origin.ncols)
cols_origin = sheet_origin.col_values(4)

j = 0
for i in range(rows_o):
    info = sheet_origin.cell_value(i,2)
    des = sheet_origin.cell_value(i,3)
    #info = "[22]sdfs"
    #print (info)
    for k in range(rows_c):
        chose = sheet_chose.cell_value(k,0)
        #print(chose)
        if (-1 != str(info).find(str(chose))):
            worksheet.write(j, 0, label = des)
            print(des)
            j = j+1 

workbook.save('Excel_Workbook.xls')

