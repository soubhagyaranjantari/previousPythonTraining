import mysql.connector


try:
    con_obj = mysql.connector.connect(host="localhost",user="root",password="root123")

    print(con_obj)
    
    if con_obj.is_connected():
        print("Connection is established")
    else:
        print("failed to establish the connection")

except Exception as ex:
    print("Error occured")
    print("Please check your credentials")