#Delete files with Extension .log
import os
DelList=[]
FDList=os.listdir()
print(FDList)
print("Files with .log extension")
for item in FDList:
    if item.endswith(".log"):
        os.remove(item)
