from db import curs, connection
def get_user():
    try:
        sql = "SELECT * FROM `users`"
        curs.execute(sql)
        connection.commit()

        data = curs.fetchall()
        return data
    except:
        return False

def get_user_by_id(id):
    try:
        sql = "SELECT * FROM `users` WHERE id = %s"
        curs.execute(sql, id)
        connection.commit()

        data = curs.fetchone()
        return data
    except:
        return False
