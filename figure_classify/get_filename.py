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
def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('E:/data/POCO/poco/voice5.xlsx');

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names();
    print(allSheetNames);

    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0];
    print(sheet1Name);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    content = workBook.sheet_by_index(0); # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    #sheet1_content2 = workBook.sheet_by_name('Sheet1');

    # 3. sheet的名称，行数，列数
    print(content.name,content.nrows,content.ncols);

    # 4. 获取整行和整列的值（数组）
    rows = content.row_values(0); # 获取第1行内容
    cols = content.col_values(0); # 获取第1列内容
    print(rows);   
    
    source ='E:\\data\\POCO\\poco\\'
    target = 'E:\\data\\poco1\\'
    for item in range(0,content.nrows):#遍历excel
        filename=content.cell(item,0).value#第一列
        voice=open('voice.txt','a')
        print('md ' +target+ filename ,file=voice)#分两步
        print('xcopy ' +source+ filename+' ' + target+filename+' /s' ,file=voice)#分两步
        voice.close();
read_excel()


