#Insert Data into mySQL DB
import pymysql

db=pymysql.connect(host="localhost",port=3306,user="root",passwd="MySQLRoot",db="schlumberger")

cursor=db.cursor()

sql="insert into employee(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values ('{}','{}',{},'{}',{})".format('Pramod','T',31,'M',15000)
        
cursor.execute(sql)
db.commit()
db.close
