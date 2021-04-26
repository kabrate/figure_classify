# -*- coding: utf-8 -*-  
import os 
import xlrd
import xlwt

def file_name(file_dir):  
    for root, dirs, files in os.walk(file_dir): 
        print(root) #当前目录路径 
        #print(dirs) #当前路径下所有子目录 
        #print(files) #当前路径下所有非目录子文件
        voice=open('voice.txt','a')
        print('copy ' +source+ root ,file=voice)
        voice.close(); 
def bat_gen(xlsx_path,source,target,bat_name):
    # 打开文件
    workBook = xlrd.open_workbook(xlsx_path);
                                                                            
    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    content = workBook.sheet_by_index(0); # sheet索引从0开始 
    for item in range(0,content.nrows):#遍历excel
        filename=content.cell(item,0).value#第一列
        voice=open(bat_name,'a')
        #print('md ' +target+ filename ,file=voice)#创建文件夹
        print('xcopy ' +source+ filename+' ' + target+filename+' /s' ,file=voice)#复制文件到新文件夹中
        voice.close();
xlsx_path='E:/data/POCO/poco/seperate1.xlsx'#excel地址
source='E:\\data\\spec\\'#文件来源的位置
target = 'E:\\data\\spec1\\true\\'#文件复制的位置
bat_name='spe_true.txt'
bat_gen(xlsx_path,source,target,bat_name)


