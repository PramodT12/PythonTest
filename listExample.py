alist=[10,20,30,30,40,30]
print ("Elements are : ",alist)
print ("First Element :", alist[0])
print("Second Element : ",alist[1])

clist=[10,30,"python","a","z",40]
print("Items inside list are :",clist)

clist[5]=clist[5]+20
print("Modified clist[5] item as :",clist[5])
print("Modified Items inside clist are :",clist)
print("Length of clist is: ",len(clist))

clist.append(50)
clist.append(90)

print("Modified Items inside clist are :",clist)
clist.extend([100,120])
print(clist)

clist.clear()
print("clist is :",clist)

print("No of occurence of 30 is : ",alist.count(30))
print("Index of 30 is :",alist.index(30))
alist.insert(10,5)
print(alist)
print("Removed value is :",alist.pop(4))
print(alist)
