#create the database
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
    cur_obj.execute("create database data1")
    print("DataBase creatred")

except:
    con_obj.rollback()

con_obj.close()


