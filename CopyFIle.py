#Copy files from one dir to another
import os,shutil,pathlib
#try:
FileList=os.listdir("C:\\Users\PTiwari9\Desktop\Test2")
DestDir="C:\\Users\PTiwari9\Desktop\Test1"
SrcDir="C:\\Users\PTiwari9\Desktop\Test2"
for item in FileList:
    item=os.path.join(SrcDir,item)
    print(item)
    shutil.copy(item,DestDir)
#except:
    print("Files Copied")
