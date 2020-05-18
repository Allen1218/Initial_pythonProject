import xlwt
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
lista=['A20041100022','A20041100025','A20041100034','A20041100039','A20041100050','A20041100060','A20041100062','A20041100067','A20041100080','A20041100081','A20041100086','A20041100089','A20041100090','A20041100091','A20041100092','A20041100093']

f= open('A1.txt', 'w')


for tmp in lista :
    f.writelines(tmp)
    f.write('\n')
    for i in range(1, 21, 1) :
        if i < 10:
            i = "00%d" % i
        elif i < 100:
            i = "0%d" % i
        else:
            i = str(i)
        lot = tmp + '.' + str(i)
        f.writelines(lot)
        # 写入excel
        # 参数对应 行, 列, 值
        f.write('\n')
    #f.write('\n')
f.close()

fopen = open('A1.txt', 'r')
lines = fopen.readlines()

j=0
for line in lines:
    sheet.write(j, 0, line)
    print(line)
    j=j+1


file.save('Excel_test.xls')