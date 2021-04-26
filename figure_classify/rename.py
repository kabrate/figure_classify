
import matplotlib.pyplot as plt
import numpy as np
import os
filepath = 'E:\\data\\spec\\'
for root, dirs, files in os.walk(filepath):   #遍历所给地址的所有文件夹和文件 root是路径 dirs路径中的子文件夹 files是路径中文件
    #print(root) #当前目录路径  
    #print(dirs) #当前路径下所有子目录  
    #print(files) #当前路径下所有非目录子文件
    if dirs:
        break
len_dirs=len(dirs)
for j in range(0,len_dirs):
    for root1, dirs1, files1 in os.walk(filepath+dirs[j]):   #遍历所给地址的所有文件夹 root是路径 dirs路径中的子文件夹 files是路径中文件
        pass
    for i in range(0,len(files1)): #文件夹中的文件
        filename = filepath+dirs[j]+'/'+files1[i]
        target=filepath+dirs[j]+'\\'+files1[i]
        newname=dirs[j]+'_'+files1[i]
        ren=open('ren.txt','a')
        print('ren ' +target+ ' '+newname ,file=ren)#分两步
        #print('xcopy ' +source+ filename+' ' + target+filename+' /s' ,file=voice)#分两步
        ren.close();
    print(str(j)+'  '+dirs[j]+'finished!')

