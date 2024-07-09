import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="New_DB"
    )
    curs = connection.cursor()
except:
     print("Connection Error!")