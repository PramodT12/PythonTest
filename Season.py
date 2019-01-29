Month=(input("Enter the Month: "))
Winter=['january','february','march']
Summer=['april','may','june']
Rainy=['july','august','september','october']
if Month.lower() in Winter:
    print("entered month is Winter Season")
elif Month.lower() in Summer:
    print("entered month is Summer Season")
elif Month.lower() in Rainy:
    print("entered month is Rainy Season")
else:
    print("Hello")
