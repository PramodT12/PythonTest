#CSV parsing using csv library

import csv
unique_cities=set()
with open("RealEstate.csv") as fobj:
    csvreader=csv.reader(fobj)
    for line in csvreader:
        city=line[1]
        unique_cities.add(city)
for city in unique_cities:
    print(city)
