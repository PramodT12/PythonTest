#Count people living in City RIO LINDA
Cities=[]
with open("RealEstate.csv") as fobj:
    line=fobj.readline()
    for line in fobj:
        line=line.strip()
        lineList=line.split(",")
        Cities.append(lineList[1])
print("Printing Cities and its Count")
CitiesSet=set(Cities)
for i in CitiesSet:
    Count=Cities.count(i)
    print(i+":"+str(Count))
