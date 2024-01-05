import mysql.connector as s
con_obj=s.connect(user='kanhu',password='kanhu',host='localhost')
cur_obj=con_obj.cursor()
cur_obj.excute('show databases')