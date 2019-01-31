#Copy content of RealEstate.csv to DB
import csv
import pymysql

def createtable():
    try:
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
        with open("RealEstate.csv") as fobj:
            Header=fobj.readline()
            csvreader=csv.reader(fobj)
            for item in csvreader:
                #print(item)
                sql="insert into RealEstate values ('{}','{}',{},'{}',{},{},{},'{}','{}',{},{},{})".format(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11])
                cursor.execute(sql)
        cursor.execute("commit")
        con.close()  

# Main Program execution :
con=pymysql.connect(user="root",passwd="MySQLRoot",host="localhost",port=3306,db="schlumberger")
cursor=con.cursor()
#createtable()
copycontent()


