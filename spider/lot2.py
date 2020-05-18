import xlrd as xlrd
import xlwt
import codecs
import csv

import  redis

#  pyinstaller -F -p C:\develop\python_3_8_2\Code\test\venv\Lib\site-packages
#  chcp 65001

print("提示：1.源文件请命名为 SourceFileName.xlsx !")
print("提示：2.输出的文件名为 OutPut_Lot.xls 和 OutPut_Lot.csv !")

strInt = input("请输入，拆分子Lot个数（表示子lot的个数）：")
print ("您输入的保留行关键字是(例如 DTPFsrv.1): ", strInt)

# 转CSV
def xlsx_to_csv():
    workbook = xlrd.open_workbook('OutPut_Lot.xls')
    table = workbook.sheet_by_index(0)
    with codecs.open('OutPut_Lot.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

SourceFileName='SourceFileName.xlsx'

#从源文件中获取数据
def GetSourceDataFromFile(fileName):
   "函数_文档字符串"
   # lot:
   dictSource={}

   # 打开文件
   data = xlrd.open_workbook(fileName)

   # 查看工作表
   sheetName = data.sheet_names()
   print("sheets：" + str(data.sheet_names()))
   # 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
   table = data.sheet_by_index(0)

   # 获取行数和列数
   # 行数：table.nrows
   # 列数：table.ncols
   print("总行数：" + str(table))
   print("总列数：" + str(table.ncols))

   # 获取整行的值 和整列的值，返回的结果为数组
   # 整行值：table.row_values(start,end)
   # 整列值：table.col_values(start,end)
   # 参数 start 为从第几个开始打印，
   # end为打印到那个位置结束，默认为none
   print("整行值：" + str(table.row_values(0)))
   print("整列值：" + str(table.col_values(1)))

   for i in range(0, table.nrows):
       row_list = table.row_values(i)

       #ProductName	WorkOrder	PanelId	MagazineId
       valueList = [row_list[1], row_list[2], row_list[3], row_list[4]]
       dictSource[row_list[0]] = valueList
       print('row_list:', row_list)

   return dictSource


file = xlwt.Workbook(encoding='utf-8', style_compression=0)
#新建一个sheet
sheet = file.add_sheet('data')
# MotherLot
# ChildLotId
# ProductName
# WorkOrder
# PanelId
# MagazineId

# Lot List
# lot :  ProductName, WorkOrder, PanelId, MagazineId
dictSource = GetSourceDataFromFile(SourceFileName)
print(dictSource)
sheet.write(0, 0, 'MotherLot')
sheet.write(0, 1, 'ChildLotId')

sheet.write(0, 2, 'ProductName')
sheet.write(0, 3, 'WorkOrder')

sheet.write(0, 4, 'PanelId')
sheet.write(0, 5, 'MagazineId')

j=1
h=1
first = 'T'
for tmp in dictSource :
    print(tmp)
    for i in range(1, int(strInt) + 1, 1) :
        if i < 10:
            i = "00%d" % i
        elif i < 100:
            i = "0%d" % i
        else:
            i = str(i)
        lot = tmp + '.' + str(i)

        # 父Lot 处理
        if first == 'T':
            sheet.write(j, 0, tmp) ###夫、 Lot
            sheet.write(j, 1, tmp) ### zi lot

            sheet.write(j, 2, dictSource[tmp][0])  ### product
            sheet.write(j, 3, dictSource[tmp][1])  ### WONumber

            sheet.write(j, 4, dictSource[tmp][2])  ### PanelId
            sheet.write(j, 5, dictSource[tmp][3])  ### MagazineId
            j = j + 1
        first = 'F'

        # 子Lot 处理
        sheet.write(j, 0, tmp)
        sheet.write(j, 1, lot)

        sheet.write(j, 2, dictSource[tmp][0])  ### product
        sheet.write(j, 3, dictSource[tmp][1])  ### WONumber

        sheet.write(j, 4, dictSource[tmp][2])  ### PanelId
        sheet.write(j, 5, dictSource[tmp][3])  ### MagazineId
        j = j + 1
    first = 'T'

file.save('OutPut_Lot.xls')
xlsx_to_csv()

