# To insert the values
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="kanhu",database="data1")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
    cur_obj.execute("insert into movies(id,name,color) values (123,'RE meteor','black')")

    con_obj.commit()
except:
    print("error occured")

print(cur_obj.rowcount,"row are inserted")

con_obj.close()