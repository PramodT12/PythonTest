#Create 10 files with .log extensions
import pathlib
NewF=""
for i in range(1,11):
    NewF=str(i)+".log"
    pathlib.Path(NewF).touch()
    
