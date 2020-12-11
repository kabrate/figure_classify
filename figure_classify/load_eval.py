import xlrd
import xlwt

def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('E:/迅雷下载/DS_10283_3336/LA/LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.eval.trl.xlsx');

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
    rows = content.row_values(3); # 获取第四行内容
    cols = content.col_values(2); # 获取第三列内容
    print(rows);
    
    source ='E:\\迅雷下载\\DS_10283_3336\\LA\\LA\\ASVspoof2019_LA_eval\\flac\\'
    target1 = ' E:\\data\\eval\\bonafide '
    target2 = ' E:\\data\\eval\\a01 '
    target3 = ' E:\\data\\eval\\a02 '
    target4 = ' E:\\data\\eval\\a03 '
    target5 = ' E:\\data\\eval\\a04 '
    target6 = ' E:\\data\\eval\\a05 '
    target7 = ' E:\\data\\eval\\a06 ' 
    target8 = ' E:\\data\\eval\\a07 ' 
    target9 = ' E:\\data\\eval\\a08 ' 
    target10 = ' E:\\data\\eval\\a09 ' 
    target11 = ' E:\\data\\eval\\a10 ' 
    target12 = ' E:\\data\\eval\\a11 ' 
    target13 = ' E:\\data\\eval\\a12 ' 
    target14 = ' E:\\data\\eval\\a13 ' 
    target15 = ' E:\\data\\eval\\a14 ' 
    target16 = ' E:\\data\\eval\\a15 ' 
    target17 = ' E:\\data\\eval\\a16 ' 
    target18 = ' E:\\data\\eval\\a17 ' 
    for item in range(0,content.nrows):
        filetype=content.cell(item,2).value
        filename=content.cell(item,1).value
        filename=filename+'.flac'
        if (filetype=='bonafide'):
            bonafide=open('bonafide.bat','a')
            print('copy ' +source+ filename + target1 ,file=bonafide)
            bonafide.close();
        elif (filetype=='A01'):
            a01=open('a01.bat','a')
            print('copy ' +source+ filename + target2 ,file=a01)
            a01.close()
        elif (filetype=='A02'):
            a02=open('a02.bat','a')   
            print('copy ' +source+ filename + target3 ,file=a02)
            a02.close()
        elif (filetype=='A03'):
            a03=open('a03.bat','a') 
            print('copy ' +source+ filename + target4 ,file=a03)
            a03.close()
        elif (filetype=='A04'):
            a04=open('a04.bat','a') 
            print('copy ' +source+ filename + target5 ,file=a04)
            a04.close()
        elif (filetype=='A05'):
            a05=open('a05.bat','a') 
            print('copy ' +source+ filename + target6 ,file=a05)
            a05.close()
        elif (filetype=='A06'):
            a06=open('a06.bat','a')
            print('copy ' +source+ filename + target7 ,file=a06)
            a06.close()
        elif (filetype=='A07'):
            a07=open('a07.bat','a')
            print('copy ' +source+ filename + target8,file=a07)
            a07.close()
        elif (filetype=='A08'):
            a08=open('a08.bat','a')
            print('copy ' +source+ filename + target9 ,file=a08)
            a08.close()
        elif (filetype=='A09'):
            a09=open('a09.bat','a')
            print('copy ' +source+ filename + target10 ,file=a09)
            a09.close()
        elif (filetype=='A10'):
            a10=open('a10.bat','a')
            print('copy ' +source+ filename + target11,file=a10)
            a10.close()
        elif (filetype=='A11'):
            a11=open('a11.bat','a')
            print('copy ' +source+ filename + target12 ,file=a11)
            a11.close()

        elif (filetype=='A12'):
            a12=open('a12.bat','a')
            print('copy ' +source+ filename + target13 ,file=a12)
            a12.close()
        elif (filetype=='A13'):
            a13=open('a13.bat','a')
            print('copy ' +source+ filename + target14 ,file=a13)
            a13.close()
        elif (filetype=='A14'):
            a14=open('a14.bat','a')
            print('copy ' +source+ filename + target15 ,file=a14)
            a14.close()
        elif (filetype=='A15'):
            a15=open('a15.bat','a')
            print('copy ' +source+ filename + target16 ,file=a15)
            a15.close()
        elif (filetype=='A16'):
            a16=open('a16.bat','a')
            print('copy ' +source+ filename + target17,file=a16)
            a16.close()
        elif (filetype=='A17'):
            a17=open('a17.bat','a')
            print('copy ' +source+ filename + target18,file=a17)
            a17.close()


    # 5. 获取单元格内容(三种方式)
    print(content.cell(1, 0).value);
    print(content.cell_value(2, 2));
    print(content.row(2)[2].value);

    # 6. 获取单元格内容的数据类型
    # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    print(content.cell(1, 0).ctype);


if __name__ == '__main__':
    read_excel();

