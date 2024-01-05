#To create the table
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
    cur_obj.execute("create table data1.movies(id int(10), name VARCHAR(20), color VARCHAR(10))")
    print("Table created")

except:
    con_obj.rollback()

con_obj.close()