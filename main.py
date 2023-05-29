import random
import pymysql
import pymysql.cursors
import re
import ssl
import smtplib
user=''
'''
    EMAIL PARAMETERS
'''
email_sender='carlosarzez25@gmail.com'
email_password='ohkkhnkblfckdmhn'
email_receiver=''
subject="Envio contraseña y password"
body=""
"""
    MQTT BROKER PARAMETERS
"""
broker = 'ec2-44-204-178-128.compute-1.amazonaws.com'
port = 1883
topic = "WSNPIIData"
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'carlos'
password = 'carlos123'
usernameDisplay=''
def obtener_conexion():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Carlos123#',
                             database='WSNProjectII')
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE password=SHA1('123')"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
if __name__ == '__main__':
    obtener_conexion()
