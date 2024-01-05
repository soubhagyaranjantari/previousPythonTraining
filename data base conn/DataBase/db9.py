# TO delete the values

import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root",database="data1")

print(con_obj)       

cur_obj = con_obj.cursor()

qry = "delete from bikes where color='grey'"

cur_obj.execute(qry)

con_obj.commit()

print(cur_obj.rowcount,"rows deleted")

con_obj.close()
