import xlrd
import xlwt

def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('E:/迅雷下载/DS_10283_3336/LA/LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.dev.trl.xlsx');

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
    
    source ='E:\\迅雷下载\\DS_10283_3336\\LA\\LA\\ASVspoof2019_LA_dev\\flac\\'
    target1 = ' E:\\data\\dev\\bonafide '
    target2 = ' E:\\data\\dev\\a01 '
    target3 = ' E:\\data\\dev\\a02 '
    target4 = ' E:\\data\\dev\\a03 '
    target5 = ' E:\\data\\dev\\a04 '
    target6 = ' E:\\data\\dev\\a05 '
    target7 = ' E:\\data\\dev\\a06 ' 
    for item in range(0,content.nrows):
        filetype=content.cell(item,2).value
        filename=content.cell(item,1).value
        filename=filename+'.flac'
        if (filetype=='bonafide'):
            bonafide=open('bonafide.txt','a')
            print('copy ' +source+ filename + target1 ,file=bonafide)
            bonafide.close();
        elif (filetype=='A01'):
            a01=open('a01.txt','a')
            print('copy ' +source+ filename + target2 ,file=a01)
            a01.close()
        elif (filetype=='A02'):
            a02=open('a02.txt','a')   
            print('copy ' +source+ filename + target3 ,file=a02)
            a02.close()
        elif (filetype=='A03'):
            a03=open('a03.txt','a') 
            print('copy ' +source+ filename + target4 ,file=a03)
            a03.close()
        elif (filetype=='A04'):
            a04=open('a04.txt','a') 
            print('copy ' +source+ filename + target5 ,file=a04)
            a04.close()
        elif (filetype=='A05'):
            a05=open('a05.txt','a') 
            print('copy ' +source+ filename + target6 ,file=a05)
            a05.close()
        elif (filetype=='A06'):
            a06=open('a06.txt','a')
            print('copy ' +source+ filename + target7 ,file=a06)
            a06.close()


    # 5. 获取单元格内容(三种方式)
    print(content.cell(1, 0).value);
    print(content.cell_value(2, 2));
    print(content.row(2)[2].value);

    # 6. 获取单元格内容的数据类型
    # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    print(content.cell(1, 0).ctype);


if __name__ == '__main__':
    read_excel();

