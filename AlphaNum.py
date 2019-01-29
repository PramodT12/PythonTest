String=input("Enter the String: ")
Alpha=0
Numeral=0
for i in String:
 if i.isnumeric():
     Numeral+=1
 elif i.isalpha():
     Alpha+=1
print("Alphabet COunt: ",Alpha)
print("Numerals count: ",Numeral)
