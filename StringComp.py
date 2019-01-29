String=input("Enter the string:")
if len(String) < 5:
    print("Length of string is too short")
elif len(String) >30:
    print("Length of string is too long")
else:
    print("Entered String has decent length:",len(String))
