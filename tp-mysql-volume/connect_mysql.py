import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,
    user='root',
    password='rootM2dsia',
    database='testdb'
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())

cursor.close()
conn.close()
