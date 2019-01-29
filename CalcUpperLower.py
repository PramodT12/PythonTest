String=input("Enter a sentence to count Upper Lower casing: ")
UCount=0
LCount=0
for item in String:
    if item.isupper():
        UCount+=1
    elif item.islower():
        LCount+=1
print("Upper Case letters: ",UCount)
print("Lower Case letters: ",LCount)
