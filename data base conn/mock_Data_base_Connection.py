import mysql.connector as s
con_obj=s.connect(user='root',password='kanhu',host='localhost')
cur_obj=con_obj.cursor()
cur_obj.execute('show databases')
print(con_obj)
print(cur_obj)
for i in cur_obj:
    print(i)