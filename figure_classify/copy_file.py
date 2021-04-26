import numpy as np
import os
import xlrd
import xlwt
xlsx_path='E:\\data\\POCO\\poco\\seperate2.xlsx'#excel地址
filepath='E:\\data\\spec\\'#源地址
target='E:\\data\\spec1\\false'#目的地址
workBook = xlrd.open_workbook(xlsx_path);
content = workBook.sheet_by_index(0); # sheet索引从0开始 
dirs={}
i=0
for item in range(0,content.nrows):#遍历excel
    dirs[i]=content.cell(item,0).value#第一列
    i=i+1
len_dirs=len(dirs)
for j in range(0,len_dirs):
    for root1, dirs1, files1 in os.walk(filepath+dirs[j]):   #遍历所给地址的所有文件夹 root是路径 dirs路径中的子文件夹 files是路径中文件
        pass
    for i in range(0,len(files1)): #文件夹中的文件
        filename = filepath+dirs[j]+'\\'+files1[i]
        newname=dirs[j]+'_'+files1[i]
        ren=open('cp.txt','a')
        print('copy ' +filename+' ' + target ,file=ren)#分两步
        ren.close();
    print(str(j)+'  '+dirs[j]+'finished!')