#To update the values
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root",database="data1")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
    cur_obj.execute("update bikes set color='grey' where color='blue'")

    con_obj.commit()
except:
    print("error occured")

print(cur_obj.rowcount,"roes is updated")

con_obj.close()