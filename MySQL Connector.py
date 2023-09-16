import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1', password='akuanakhebat', user = 'root')

if conn.is_connected():
    print("Connection established.....")