#功能：
#将txt文件中的各子卡信息存入des.excel中
#excel存入格式
#
#cardId  slot Tx(第一个) Rx（第二个）
#0        2    -2        0
#1        2
#2        2
#3        2

#命令行提取格式
#display optical-module extend information slot 3 card 0 | no-more

#存储格式
#slot/card/port    lane    TX     RX
#3/0/0             1    0.491     1.013
#3/0/0             2    1.222     2.133
#3/0/0             3    2.253     7.323
#3/0/0             total 4
#3/0/1             1
#3/0/1             2
#3/0/1             3 
#3/0/1             total 

import sys
import xlwt
import re
import datetime
import xlrd

#读文件
excel = xlrd.open_workbook('excelFile.xls')
worksheet = excel.sheets()[0]
col = worksheet.ncols


zero = 1 +col               #slot/card/port
one = 2 + col                #lane
two = 3 + col                #Tx
three = 4 +col              #Rx


#cur_time = datetime.datetime.now()
#pattern_sh_name = '\d{4}-\d{2}-\d{2}'
#pattern_hour = '\d{2}:\d{2}:\d{2}' 
#name1 = str(re.match(pattern_sh_name,str(cur_time)).group())
#name2 = str((re.search(pattern_hour,str(cur_time)).group()).replace(':','-'))

#name = name1 +'-' + name2
#print (name)
#读源数据文件
#f = open(r"data.txt","r")
#line = f.readline()
#print (line)
#写目标文件

#创建流程
#workbook = xlwt.Workbook(encoding = 'ascii')

#打开
#workbook = xlrd.open_workbook('Ori_data.xls')

#worksheet = workbook.add_sheet(str(name1))
#正则表达式
#pattern = 'Tx1([\s]+-[\d]+){3}[\s]+[\w]+'
#完整匹配 display optical-module extend information slot 3 card 0 | no-more
pattern_cmd = '.*dis[a-zA-Z]*[\s]+o[\S]*[\s]+e[a-zA-Z]*[\s]+i[a-zA-Z]*[\s]+s[a-zA-Z]*[\s]+[\d]+[\s]+c[a-zA-Z]*[\s]+[\d]+[\s]+\|[\s]+n[\S]*'
#匹配Car0-Port0
pattern_Card = 'Card[\d]*-Port[\d]+\s+\+[\s]+Valu'
pattern_Tx = '.*Tx Power Lane[\d]+\(.+\)[\s]+-?[\d]+[\.]?[\d]*[\s]+'
pattern_Rx = '.*Rx Power Lane[\d]+\(.+\)[\s]+-?[\d]+[\.]?[\d]*[\s]+'
pattern_Lan = '.*Lane[\d]+'
pattern_tx_total = '.*Tx[\s]+Power[\s]+Total\(.+\)[\s]+'
pattern_rx_total = '.*Rx[\s]+Power[\s]+Total\(.+\)[\s]+'
pattern_num = '-?\d+\.?\d*'


#re.match(pattern, line, flags=0)     #匹配成功与否的标志位
i = 1    #行
j = 0    #列

#先写表头
worksheet.write(0,zero,label = 'port')
worksheet.write(0,one,label = 'lane')
worksheet.write(0,two,label = 'Tx')
worksheet.write(0,three,label = 'Rx')

slot = 0
card = 0
port = 0

first_match_tx = 1

while line:
    #print(line)
    if (re.findall(pattern_cmd, line)):
        m = re.findall(pattern_num,line)
        ##print (m)
        slot = m[0]
        ##print (slot)
        
        card = m[1]
        #print (card)
    elif (re.findall(pattern_Card, line)):
        m = re.findall(pattern_num,line)
        port = m[1]
    elif (re.findall(pattern_Tx, line)):
        m = re.findall(pattern_num,line)
        #print(m)
        b = str(slot)+'/'+str(card)+'/'+str(port)
        worksheet.write(i,zero,label = b)
        #print(b)
        #print(m)
        worksheet.write(i,one,label = m[0])
        worksheet.write(i,two,label = m[1])
        
        i = i+1
        #print (i)
        #print (m[0])
        #print (m[1])
        #print (m[2])
    elif (re.findall(pattern_tx_total, line)):
        m = re.findall(pattern_num,line)
        worksheet.write(i,zero,label = str(slot)+'/'+str(card)+'/'+str(port))
        worksheet.write(i,one,label = 'total')
        j = i
        worksheet.write(i,two,label = m[0])
        i = i+1
        #print (i)
        #print (j)
        #print (m[0])
    elif (re.findall(pattern_Rx, line)):
        m = re.findall(pattern_num,line)
        worksheet.write(first_match_tx,three,label = m[1])
        first_match_tx += 1
        #print (i)
        #print (m[0])
        #print (m[1])
        #print (m[2])
    elif (re.findall(pattern_rx_total, line)):
        m = re.findall(pattern_num,line)
        worksheet.write(j,three,label = m[0])
        first_match_tx += 1
        #print (i)
        #print (j)
        #print (m[0])
    line = f.readline()
workbook.save('Excel_Workbook.xls')
f.close()
