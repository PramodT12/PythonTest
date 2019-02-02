import os

status=os.system("bash hello")
print(status)
if status == 0:
    print("Successful")
else :
    print("Something went wrong")
