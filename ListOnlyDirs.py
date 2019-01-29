#List only Directories
import os
Dir="C:\\"
DirL=[]
FDList=os.listdir(Dir)
print(FDList)
for i in FDList:
    if os.path.isdir(os.path.join(Dir,i)):
        DirL.append(i)
print("DIrectories List :",DirL)

