#Test Excel with Openpyxl library
from openpyxl import Workbook
wb=Workbook()
ws=wb.active

ws['A1']=42

ws.append([1,2,3])
ws.append([1,2,3,4])
import datetime
Date=datetime.datetime.now()
ws.append([Date])

wb.save("TestXL.xlsx")
