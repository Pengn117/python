import xlrd  
import xlwt
from xlutils.copy import copy        #导入copy模块

import os


filename = "chose_tcl.txt" #相对路径,文件在.py文件所在的目录中    
    

#搜索excel中关键字是否在txt中存在，若存在是否连跑设置Y
def SearchFilesContent():
    print("search begin")

    data_origin = xlrd.open_workbook('origin.xls')
    sheet_origin = data_origin.sheet_by_name(u'Sheet1')
    rows_o = sheet_origin.nrows
    print("rows_o = %d" %rows_o)
    cols_o = sheet_origin.ncols

    #修改部分
    wb = copy(data_origin) 
    ws = wb.get_sheet('Sheet1')                   #获取表单

    #ws.write(0, 0, 'changed!')             #改变（0,0）的值
    #ws.write(8,0,label = '好的')           #增加（8,0）的值
    
    #1.打开txt文件
    FileObj = open(filename)
    k = 0
    rowDict = {}
    for line in FileObj.readlines():
        # 把每一行转换成一个字典，便于直接利用sklearn直接提供的库函数
        rowDict[k] = line
        print("rowDict = " +rowDict[k])
        k = k + 1
        
    FileObj.close()


        
    print("1")
    #2.读取行信息
    #LineTemp = FileObj.readlines()
    print("2")
    for i in range(rows_o):
        KeyStr = sheet_origin.cell_value(i,3)
        print("KeyStr = " + KeyStr)
        for j in rowDict:
            #3.是否包含关键字
            #4.不包含则循环操作，包含的话将行显示，并修改并行连跑字段Y
            # print("i = %d" %i)
            #print("line = " + line)
            if rowDict[j].find(KeyStr) != (-1):
                if ('Y' != sheet_origin.cell_value(i,5)):
                    ws.write(i, 5, 'Y')             #改变（0,0）的值
                    #sheet_origin.write(i, 5, 'Y')
                    print("write sucess !name = " + KeyStr)
                    break
            
    
    #data_origin.save('origin.xls')    
    #data_origin.close()
    wb.save('weng.xls')                    #保存文件            
    print("search end = ")




#仅当本python模块直接执行时，才执行如下语句，若被别的python模块引入，则不执行
if __name__ == '__main__':
    SearchFilesContent()
