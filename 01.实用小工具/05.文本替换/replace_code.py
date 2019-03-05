import re

dirfile = "operate_file.c"




def test():
    data = []
    for line in open(dirfile,"rb"): #设置文件对象并读取每一行文件
        #print line.decode='gb18030'
        #print(line.decode='gb18030')
        print(line.decode('gb18030'))
        #print(line)

def My_match():
    str_ori = "www.baidu.com"
    keyword = r"badi"
    t = re.search(keyword, str_ori, flags=0) 
    print (t)

if __name__ == '__main__':
    test()
    #My_match()
