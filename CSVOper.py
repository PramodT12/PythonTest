#Program to display Unique Cities from RealEstate.csv
CitySet=set()
with open("RealEstate.csv") as fobj:
    for line in fobj:
        line=line.strip()
        lineList=line.split(",")
        CitySet.add(lineList[1])
#Print Unique Cities

for item in CitySet:
    print(item)

print("Now printing using DIctonary")
#2nd Way
UniqueDict={}
with open("RealEstate.csv") as fobj:
    line=fobj.readline()
    for line in fobj:
        line=line.strip()
        lineList=line.split(",")
        UniqueDict[lineList[1]]=1
for city in UniqueDict:
    print(city)
