#Create Table in MySQL DB

import pymysql

#Open DB Connection
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="MySQLRoot",db="schlumberger")

#Prepare the cursor object using cursor() method
cursor=db.cursor()

#Drop table if it exists already using execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Create table

sql="""CREATE TABLE EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""
cursor.execute(sql)
print("Table created successfully")

#Disconnect from server
db.close()
