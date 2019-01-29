String=input("Enter the string to be reversed : ")
ListStr=list(String)
ListStr.reverse()
StringUp="".join(ListStr)
print("Reverse of string is: ",StringUp)
#Other Method using string
print(String[::-1])
