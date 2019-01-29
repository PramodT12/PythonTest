alist=[]
print(alist)
alist.append(10)
print("Append 10 to list",alist)
alist.append(20)
print("Append 20 to list",alist)
alist.append(50)
print("Append 50 to list",alist)
alist.extend([90,20,45,32,645,32,90,65,43,55,4,32,50])
print("List extended: ",alist)
alist=list(set(alist))

print("Final output :",alist)
print("Removing duplicates:",alist)
alist.remove(50)
print(alist)


