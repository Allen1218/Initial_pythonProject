import xlwt

SourceFileName='SourceFileName.xls'

def GetSourceDataFrom( fileName ):
   "函数_文档字符串"
   dictSource={}

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
# lista=['A20041100022','A20041100025']
lista={'A20041100022':['HA180104020769', 'HT04'],
       'A20041100025':['HA180104020725', 'HT04'],
       'A20041100034':['HA180104020517', 'HT04'],
       'A20041100039':['HA180104020474', 'HT04'],
       'A20041100050':['HA18010402075C', 'HT04'],

       'A20041100060':['SA180221C000QN', 'HT04'],
       'A20041100062':['HA180104020501', 'HT04'],
       'A20041100063':['SA180221C000MA', 'HT04'],
       'A20041100067':['SA180221C000G4', 'HT04'],
       'A20041100068':['HA180104020626', 'HT04'],

       'A20041100080':['SA180221C000Q3', 'HT04'],
       'A20041100081':['SA180221C000Q7', 'HT04'],
       'A20041100082':['SA180221C000QT', 'HT04'],
       'A20041100086':['SA180221C000FR', 'HT04'],
       'A20041100087':['SA180221C000H7', 'HT04'],

       'A20041100089':['SA180221C000R3', 'HT04'],
       'A20041100090':['SA180221C000DG', 'HT04'],
       'A20041100091':['NA180103500532', 'HT04'],
       'A20041100092':['SA180221C000DD', 'HT04'],
       'A20041100093':['SA180221C000PL', 'HT04']}
listHeader=['122-000000-K68H', 'SP104-200400004']
# f= open('A1.txt', 'w')

sheet.write(0, 0, 'MotherLot')
sheet.write(0, 1, 'ChildLotId')

sheet.write(0, 2, 'ProductName')
sheet.write(0, 3, 'WorkOrder')

sheet.write(0, 4, 'PanelId')
sheet.write(0, 5, 'MagazineId')

j=1
h=1
first = 'T'
for tmp in lista :
    for i in range(1, 21, 1) :
        if i < 10:
            i = "00%d" % i
        elif i < 100:
            i = "0%d" % i
        else:
            i = str(i)
        lot = tmp + '.' + str(i)

        # 父Lot 处理
        if first == 'T':
            sheet.write(j, 0, tmp)
            sheet.write(j, 1, tmp)

            sheet.write(j, 2, listHeader[0])  ### product
            sheet.write(j, 3, listHeader[1])  ### WONumber

            sheet.write(j, 4, lista[tmp][0])  ### PanelId
            sheet.write(j, 5, lista[tmp][1])  ### MagazineId
            j = j + 1
        first = 'F'

        # 子Lot 处理
        sheet.write(j, 0, tmp)
        sheet.write(j, 1, lot)

        sheet.write(j, 2, listHeader[0])  ### product
        sheet.write(j, 3, listHeader[1])  ### WONumber

        sheet.write(j, 4, lista[tmp][0])  ### PanelId
        sheet.write(j, 5, lista[tmp][1])  ### MagazineId
        j = j + 1
    first = 'T'

file.save('Excel_test.xls')

