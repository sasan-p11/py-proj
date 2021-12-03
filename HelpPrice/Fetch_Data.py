from __future__ import print_function
import mysql.connector


def Fetch_Data():

    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="890073570",
        database="MyPractice"
    )
    cursor = cnx.cursor()

    sqlCon = "SELECT * FROM truecar"
    cursor.execute(sqlCon)
    myresult = cursor.fetchall()

    cursor.close()
    cnx.close()

    return myresult


