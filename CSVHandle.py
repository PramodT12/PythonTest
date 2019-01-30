#Program to read and display content of RealEstate.csv file
fobj=open("RealEstate.csv","r")
for item in fobj:
    item=item.strip()
    print(item)
fobj.close()
