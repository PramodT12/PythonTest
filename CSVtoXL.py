#Copying data from CSV to Xls
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
with open("RealEstate.csv") as fobj:
    for item in fobj:
        item=item.strip()
        line=item.split(",")
        ws.append(line)
wb.save("RealEstate.xlsx")


