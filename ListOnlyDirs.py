#List only Directories
import os
TxtL=[]
PyL=[]
FDList=os.listdir()
for i in FDList:
    if ".txt" in i:
        TxtL.append(i)
    elif ".py" in i:
        PyL.append(i)
print("Txt Files :",TxtL)
print("Python files :",PyL)
