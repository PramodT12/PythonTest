String=input("Enter the password:")
HashCount=String.count("#")
print("HashCount:",HashCount)
DollarCount=String.count("$")
print("DollarCount:",DollarCount)
AtCount=String.count("@")
print("AtCount:",AtCount)
LengthStr=len(String)
print("String Length:",LengthStr)
if (HashCount > 0 or DollarCount > 0 or AtCount > 0 ) and (len(String) >=6 and len(String) <=12):
    print("Valid Password")
else:
    print("Invalid Password")
    
        
