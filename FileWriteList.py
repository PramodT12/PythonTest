#Write list of current files and dirs in a file with name as today's date
#Validation:
#If file doesn't exists : create file
#If file exists :DIsplay error msg and exit
import os,sys
import time

Fname=time.strftime('%d%b%Y.log')

if os.path.isfile(Fname):
    print("FIle already exists with the same name: ",Fname)
    sys.exit(1)
else:
    fobj=open(Fname,"w")
    ListCUrrFiles=os.listdir()
    print("Printing Current FIles and dirs to "+Fname)
    for item in ListCUrrFiles:
        fobj.write(item+"\n")
    fobj.close()

