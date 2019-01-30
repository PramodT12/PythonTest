fobj=open("TestFile.txt","r")
for item in fobj:
    item=item.strip()
    print(item)
fobj.close()
