initStr="172.168."
for i in range(2):
    NewStr=(initStr+str(i))
    for j in range(1,11):
        print(NewStr+"."+str(j))
