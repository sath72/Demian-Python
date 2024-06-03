import mysql.connector

config={
    'user':'root',
    'password':'!QAZ2wsx',
    'host':'localhost',
    'database':'pydb',
    'port':'3306'
}
def getConn():
    conn=mysql.connector.connect(**config)
    return conn

