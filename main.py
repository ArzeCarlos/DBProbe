from flask import Flask, render_template, request,redirect,url_for,session
from flask_socketio import SocketIO
from threading import Lock
from datetime import datetime
from paho.mqtt import client as mqtt_client
from email.message import EmailMessage
import random
import json
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
            sql = "SELECT * FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
if __name__ == '__main__':
    obtener_conexion()
