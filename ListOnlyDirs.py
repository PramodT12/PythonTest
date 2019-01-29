#List only Directories
import os
DirL=[]
FDList=os.listdir("C:\\")
print(FDList)
for i in FDList:
    i='C:\\'+i
    if os.path.isdir(i):
        DirL.append(i)
print("DIrectories List :",DirL)

