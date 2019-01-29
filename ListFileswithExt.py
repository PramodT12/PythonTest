#List files with .py and .txt only
import os
TxtL=[]
PyL=[]
FDList=os.listdir()
for i in FDList:
    if i.endswith(".txt"):
        TxtL.append(i)
    elif i.endswith(".py"):
        PyL.append(i)
print("Txt Files :",TxtL)
print("Python files :",PyL)
