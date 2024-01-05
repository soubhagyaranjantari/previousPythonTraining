#To insert multiple values
import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",password="root")

print(con_obj)       

cur_obj = con_obj.cursor()

try:
    qry = "insert into data1.movies(id,name,color) values (%s,%s,%s)"
    vals = [
        (124,"RE classic","white"),
        (125,"RE continental","blue"),
        (126,"RE bullet","Red"),
        (127,"Bajaj Dominor","Green"),
        (128,"TVS RTR","Blue")    
    ]
    cur_obj.executemany(qry,vals)

    con_obj.commit()
except:
    print("error occured")

print(cur_obj.rowcount,"row inserted")

con_obj.close()