#Print even number 500 to 300 to filename as today's timestamp
import time

Fname=time.strftime('%d%b%Y.log')
fobj=open(Fname,"w")
for item in range(500,299,-2):
    fobj.write(str(item)+"\n")
fobj.close()
