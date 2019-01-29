String=input("Enter the String: ")
ListStr=list(String)
Alpha=0
Numeral=0
for i in ListStr:
 if str(i).isnumeric():
     Numeral+=1
 elif str(i).isalpha():
     Alpha+=1
print("Alphabet COunt: ",Alpha)
print("Numerals count: ",Numeral)
