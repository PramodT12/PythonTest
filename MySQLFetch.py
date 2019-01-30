#Fetch Data from DB
import pymysql

db=pymysql.connect(host="localhost",port=3306,user="root",passwd="MySQLRoot",db="schlumberger")

cursor=db.cursor()

sql="""select empid from empdb"""
data=cursor.execute(sql)
row = cursor.fetchone()
for item in row :
    print (item)
print("Data in EMPDB is :",data)
print(data)
db.close
