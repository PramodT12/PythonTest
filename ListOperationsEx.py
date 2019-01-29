alist = ["google.com","unix.com","facebook.com","google.com","linkedin.com"]
lenlist=[]
alist=list(set(alist))
print(alist)
for item in alist:
    lenlist.append(len(item))
print(lenlist)
