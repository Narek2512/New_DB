import requests
from fastapi import FastAPI, Request
import uvicorn
from sql import get_user
from sql import get_user_by_id
from db import curs, connection
from pydantic import BaseModel
app = FastAPI()

# @app.get('/user_info')
# def user_info():
#     i = get_user()
#     data = []
#     for x in i:
#         data.append({
#             "id": x[0],
#             "Name": x[1],
#             "Surname": x[2],
#             "Email": x[3],
#             "Password": x[4],
#             "Balance": x[5],
#             "Country": x[6],
#             "Symbol": x[7],
#             "Value": x[8]
#         })
#     return data
#
#
#
# @app.get('/country_info')
# def country_info():
#     return {
#         "Country": "USA",
#         "Capital": "Washington",
#         "Largest city": "New York City",
#         "Official languages": "None at the federal level",
#         "National language": "English",
#         "Government": "Federal presidential republic",
#         "Total area": "9,833,520 km2",
#         "Currency": "U.S. dollar ($) (USD)",
#         "Time zone": "UTC−4 to −12, +10, +11",
#         "Driving side": "right",
#         "Calling code": "+1",
#     }
#
# @app.get('/house_info')
# def house_info():
#     return {
#         "Страна": "ОАЭ",
#         "Город": "Дубай",
#         "Количество комнат": "4",
#         "Площадь, м²": " 609",
#         "Этажей в доме": "3",
#         "Количество санузлов": "4 и больше",
#         "Мебель": "Кухня, Ванная",
#         "Удобства": "Бытовая техника, Кондиционер, Гардеробная, Панорамные окна, Спортзал, Консьерж",
#         "Инфраструктура": " Магазин, Аптека, Детский сад, Школа",
#         "Во дворе": "Закрытая территория, Детская площадка, Спортивная площадка, Зоны отдыха, Бассейн",
#         "Парковка": "Открытая, Закрытая",
#         "Право на ВНЖ": "Есть",
#         "Гражданство при покупке": "Нет",
#         "Условия покупки": "Возможна ипотека, Есть рассрочка, Можно оплатить в рублях, Доступна дистанционная покупка",
#         "Инвестиции": "Услуги сдачи в аренду",
#         "Цена": "338 621 689 ₽"
#
#     }

#
# @app.post('/get_user/{name}')
# def user_info(name: str):
#     data = get_user()
#     info = []
#     for i in data:
#         name1 = i[1].lower()
#         if name1.startswith(name.lower()):
#             info.append(i)
#
#
#     return {"data": info}
#
#
# @app.post('/create_message/{id}/{Model}/{Description}/{Price}')
# def add_message(id: int, Model: str, Description: str, Price: int):
#      sql = "INSERT INTO `messages` (`id`,`Model`,`Description`,`Price`) VALUES (%s,%s,%s,%s)"
#      curs.execute(sql, (id, Model, Description, Price))
#      connection.commit()
#      return True



# @app.post('/item')
# def get_item(request: Request):
#     data = request.json()
#     password = data.
#

# class signup(BaseModel):
#     name: str
#     surname: str
#     age: int
#     email: str
#     password: str
#
# @app.post('/signup')
# def signup(info: signup):
#     if info.age < 18:
#         return {"Success": False, "message": "age lower than 18"}
#     sql = "INSERT INTO `users_2` (`name`,`surname`,`age`,`email`,`password`) VALUES (%s,%s,%s,%s,%s)"
#     curs.execute(sql, (info.name, info.surname, info.age, info.email, info.password))
#     connection.commit()
#
#     return {"Succes": True}
#
#
# class signin(BaseModel):
#     email: str
#     password: str
#
# @app.post('/signin')
# def signin(userdata: signin):
#     sql = "SELECT * FROM `users_2` WHERE `email` = %s AND `password` = %s"
#     curs.execute(sql, (userdata.email, userdata.password))
#     connection.commit()
#     data = curs.fetchone()
#     return data















# ip_address = requests.get('https://api.ipify.org').text
# print(ip_address)
#
#
# location = requests.get(f'https://ipinfo.io/{ip_address}/json').json()
# print(f"""
# Ip = '{location["ip"]}'
# Country = '{location["country"]}'
# """)
#
#
#
# res  = requests.get(f'https://restcountries.com/v3.1/alpha/{location["country"]}').json()
# currencies = res[0]['currencies']
# print(currencies)
# currencies_code = currencies.keys()
# print(currencies_code)
#
# for code in currencies_code:
#     currencies_code = code
#
# print(currencies_code)
# print(currencies[currencies_code]['symbol'])
# ###############################################
#
# user_balance = 5000

# value = 'USD'
# to_user_value = 'AMD'
#
# data = requests.get(f"https://open.er-api.com/v6/latest/{value}").json()
# print(f"1{value} = {data['rates'][to_user_value]}{to_user_value}")
# print()
#











# x = requests.get("https://service.homely.am/api/items/modern")
# x = x.json()
# print(x['all_items'])
# try:
#     print(f"""
# --------------------------------------------------
# ${x['all_items'][0]['price']}  Հատուկ    Վաճառք
# 3 / 6   3   73 ք․մ   1   {x['all_items'][0]['id']}
# --------------------------------------------------
# 📍{x['all_items'][0]['street']}
# --------------------------------------------------
# Նկարագրություն
# {x['all_items'][0]['description']}
# --------------------------------------------------
# Շրջան ------ {x['all_items'][0]['region']}                        ✅{x['all_items'][0]['conveniences'][0]}
#                                             ✅{x['all_items'][0]['conveniences'][1]}
# Շենքի տիպը ------ {x['all_items'][0]['type_of_building']}                  ✅{x['all_items'][0]['conveniences'][2]}
#                                             ✅{x['all_items'][0]['conveniences'][3]}
# Կարգավիճակ ------ {x['all_items'][0]['status']}           ✅{x['all_items'][0]['conveniences'][4]}
#
# Պատշգամբ ------ {x['all_items'][0]['balcony']}                ✅{x['all_items'][0]['facilities_in_the_building'][0]}
#                                             ✅{x['all_items'][0]['facilities_in_the_building'][1]}
# Կահույք ------ {x['all_items'][0]['furniture']}                       ✅{x['all_items'][0]['facilities_in_the_building'][2]}
#                                             ✅{x['all_items'][0]['facilities_in_the_building'][3]}
#
#
# Owner name: {x['all_items'][0]['owner_name']}
# Owner phone: {x['all_items'][0]['owner_phone']}
#
# """)
# except:
#     print("Error")






# location = requests.get('https://restcountries.eu')
# print(location)





# class reg_auto(BaseModel):

#     mark: str
#     model: str
#     year: int
#     engine_size: str
#     transmission: str
#     mileage: str
#     color: str
#     price: str

# @app.post('/reg_auto')
# def regauto(info: reg_auto):
#     sql = "INSERT INTO `cars` (`mark`,`model`,`year`,`engine_size`,`transmission`,`mileage`,`color`,`price`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
#     curs.execute(sql, (info.mark, info.model, info.year, info.engine_size, info.transmission, info.mileage, info.color, info.price))
#     connection.commit()
#     return {"success": True}
#
#
# class get_auto(BaseModel):
#     mark: str
#     model: str
#     year: int
#
# @app.post('/get_auto')
# def getauto(get: get_auto):
#     sql = "SELECT * FROM `cars` WHERE mark = %s AND model = %s AND year = %s"
#     curs.execute(sql, (get.mark, get.model, get.year))
#     connection.commit()
#     data = curs.fetchall()
#
#     return data
        # "mark": data[1],
        # "model": data[2],
        # "year": data[3],
        # "engine_size": data[4],
        # "transmission": data[5],
        # "mileage": data[6],
        # "color": data[7],
        # "price": data[8]



# class delete(BaseModel):
#     id: int
#     user_password: int
#
#
# @app.delete('/delete')
# def del_user(delete: delete):
#     sql = "SELECT * FROM `users` WHERE `id` = %s AND `user_password` = %s"
#     curs.execute(sql, (delete.id, delete.user_password))
#     connection.commit()
#     data = curs.fetchone()
#
#     if data:
#         sql = "DELETE FROM `users` WHERE `id` = %s"
#         curs.execute(sql, delete.id)
#         connection.commit()
#         return {"success": True}
#     else:
#         return {"success": False, "Error": "Wrong id or password"}




class add_workers(BaseModel):
    my_password: str
    id: int
    name: str
    surname: str
    password: str

@app.post("/add_worker")
def add_worker(add: add_workers):
    sql = "INSERT INTO `users` (`name`,`surname`,`password`,`status`) VALUES (%s,%s,%s,%s)"
    if add.my_password == "1111":
      curs.execute(sql, (add.name, add.surname, add.password, "worker"))

      connection.commit()
      return {"success": True}
    else:
        return {"success": False}


class delete(BaseModel):
    id: int
    my_password: str


@app.delete("/delete_worker")
def delete_worker(delete: delete):
    sql = "SELECT * FROM `users` WHERE `id` = %s"
    curs.execute(sql, delete.id)
    connection.commit()
    data = curs.fetchone()
    if data:

        if delete.my_password == "1111":
            sql = "DELETE FROM `users` WHERE `id` = %s"
            curs.execute(sql, delete.id)
            connection.commit()
            return {"success": True}
        else:
            return {"success": False}



class works(BaseModel):
    my_password: str
    work_to: int
    description: str


@app.post("/send_work")
def send_work(send: works):
    sql = "INSERT INTO `works` (`work_to`,`description`,`status`) VALUES (%s,%s,%s)"
    if send.my_password == "1111":
        curs.execute(sql, (send.work_to, send.description, False))
        connection.commit()
        return {"success": True}
    else:
        return {"success": False}




class login(BaseModel):
    name: str
    password: str
@app.post("/login")
def log_in(login: login):
    sql = "SELECT * FROM `users` WHERE `name` = %s AND `password` = %s"
    curs.execute(sql, (login.name, login.password))
    connection.commit()
    data = curs.fetchone()

    if data:
        sql = "SELECT * FROM `works` WHERE `work_to` = %s"
        curs.execute(sql, data[0])
        connection.commit()
        work = curs.fetchall()

        return {"Works": work[0][2]}
    else:
        return {"success": False}


class done(BaseModel):
    name: str
    password: str
    work_id: int

@app.post("/work_done")
def done(work_done: done):
    sql = "SELECT * FROM `users` WHERE `name` = %s AND `password` = %s"
    curs.execute(sql, (work_done.name, work_done.password))
    connection.commit()
    data = curs.fetchone()

    sql = "SELECT * FROM `works` WHERE `id` = %s"
    curs.execute(sql, work_done.work_id)
    connection.commit()
    data2 = curs.fetchone()

    if data and data2:
        sql = "UPDATE `works` SET `status` = %s WHERE `id` = %s"
        curs.execute(sql, (True, work_done.work_id))
        connection.commit()
        return {"success": True}
    else:
        return {"success": False}



class admin_login(BaseModel):
    password: str

@app.post("/done_works")
def done_works(done: admin_login):
    if done.password == "1111":
        sql = "SELECT * FROM `works` WHERE `status` = %s"
        curs.execute(sql, True)
        connection.commit()
        data = curs.fetchall()
        return {"Done works": data}
    else:
        return {"success": False}



class login_admin(BaseModel):
    password: str



@app.post("/not_done_works")
def not_done(not_done: login_admin):
    if not_done.password == "1111":
        sql = "SELECT * FROM `works` WHERE `status` = %s"
        curs.execute(sql, False)
        connection.commit()
        data = curs.fetchall()
        return {"Not done works": data}
    else:
        return {"success": False}




class best_worker(BaseModel):
    password: str


@app.post("/best_worker")
def best_worker(best: best_worker):
    if best.password == "1111":

        sql = "SELECT * FROM `users`"
        curs.execute(sql)
        connection.commit()
        data2 = curs.fetchone()

        sql = "SELECT * FROM `works` WHERE `status` = %s AND `id` = %s"
        curs.execute(sql, (True, data2[0]))
        connection.commit()

        data = curs.fetchall()



        return {"done": data}



    else:
        return {"success": "Incorrect password"}









uvicorn.run(app, host="127.0.0.1", port=1234)