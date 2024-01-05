#show the database
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="kanhu")

print(con_obj)       

cur_obj = con_obj.cursor()
print(dir(cur_obj))
try:
    cur_obj.execute("show databases")

except Exception as ex:
    con_obj.rollback()

for db in cur_obj:
    print(db)

con_obj.close()