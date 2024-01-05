import mysql.connector as s
try:
    con_obj = s.connect(user='root', password='kanhu',
                        host='localhost', database='sakila')
    # print(con_obj)
except Exception as e:
    print((e))
else:
    cur_obj = con_obj.cursor()
    cur_obj.execute("select * from actor ")
print(True)
print(cur_obj)
