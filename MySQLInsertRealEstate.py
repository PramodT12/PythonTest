#Copy content of RealEstate.csv to DB
import csv
import pymysql

def createtable():
    try:
        con=pymysql.connect(user="root",passwd="MySQLRoot",host="localhost",port=3306,db="schlumberger")
        cursor=con.cursor()
        cursor.execute("DROP TABLE IF EXISTS RealEstate")
        sql="""CREATE TABLE RealEstate (
        street varchar(200),
        city varchar(200),
        zip int,
        state varchar(200),
        beds int,
        baths int,
        sq__ft float,
        type varchar(200),
        sale_date varchar(200),
        price float,
        latitude float,
        longitude FLOAT)"""
        cursor.execute(sql)
    except :
        print("Error in table creation :")
    else :
        print("Table created successfully")
    finally :
        con.close()
        
def copycontent():
    try:
        con=pymysql.connect(user="root",passwd="MySQLRoot",host="localhost",port=3306,db="schlumberger")
        cursor=con.cursor()
        with open("RealEstate.csv") as fobj:
            csvreader=csv.reader(fobj)
            for item in csvreader:
                sql="insert into RealEstate values "+(item)
    except :
        print("Error in inserting values to table")
    else :
        print("Data inserted successfully")
            
    finally :
        con.close()  

createtable()
copycontent()


