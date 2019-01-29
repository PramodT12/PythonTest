#Create logfile with today's timstamp
#29_jan_2019.log and 29012019155323.log
import pathlib
import datetime
now = datetime.datetime.now()
#now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
#2017-09-20T11:52:32-98
Time=now.strftime('%d%m%Y%H%M%S.log')
print("Current Time is :",Time)
Time1=now.strftime('%d_%b_%Y.log')
print("New Time:",Time1)
pathlib.Path(Time).touch()
pathlib.Path(Time1).touch()
