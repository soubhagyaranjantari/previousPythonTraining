#TO read the values
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
   #cur_obj.execute("select * from data1.bikes")
   cur_obj.execute("select * from data1.bikes where color='blue'")

except:
    print("error occured")

for val in cur_obj:
    print(val)

con_obj.close()