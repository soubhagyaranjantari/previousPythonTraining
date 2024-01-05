import mysql.connector as s
try:
    con_obj=s.connect(host='localhost',user='root',password='kanhu')
    print(con_obj)
except Exception as e:
    print(e)
else:
    cur_obj=con_obj.cursor()
    cur_obj.execute('create database sky')
    con_obj.commit()
    