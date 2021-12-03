from __future__ import print_function
import mysql.connector


def save_result(cars):

    names = []
    list_models = []
    karkard = []
    prices = []

    for item in cars:
        names.append(item[0])
        list_models.append(item[1])
        karkard.append(item[2])
        prices.append(item[3])

    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="890073570",
        database="MyPractice"
    )
    cursor = cnx.cursor()

    for i in range(names.__len__()):
        sqlVal = (names[i], list_models[i], karkard[i], prices[i])
        sqlCon = """INSERT INTO truecar 
              (car, model, karkard, price) 
              VALUES (%s, %s, %s, %s)"""
        cursor.execute(sqlCon, sqlVal)
        cnx.commit()

    cursor.close()
    cnx.close()
    print("ok")
