#Program to check the Virtual Memory, Swap Memory and trigger the mail if value is
# VM > 90%
#Swap Memory > 95%
#Disk Utilization >70%

import psutil
import smtplib

VMem=psutil.virtual_memory()
DUse=psutil.disk_usage("C:")
SwapMem=psutil.swap_memory()

print("VMem :",VMem[2])
print("Disk Usage :",DUse[3])
print("Swap Memory:",SwapMem[3])

if float(VMem[2]) > 49.0:
    print("Sending mail as Vm is greater then threshold")
if float(DUse[3]) > 35.0:
    print("Sending mail as Disk utilization is greater then threshold")
if float(SwapMem[3]) > 50:
    print("Sending mail as Swap utilization is greater then threshold")
