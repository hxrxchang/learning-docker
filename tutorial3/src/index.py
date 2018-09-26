import os
from bottle import route, run
import mysql.connector

connector = mysql.connector.connect(
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASS'],
            host=os.environ['MYSQL_HOST'],
            database=os.environ['MYSQL_DB'])

cursor = connector.cursor()
cursor.execute('select * from books')

data = ''
for row in cursor.fetchall():
    data += 'ID:' + str(row[0]) + ' タイトル:' + row[1] + '<br> '

cursor.close
connector.close

@route('/')
def hello():
    return '<p>bottle is running<br>' + data + '</p>'

run(host='0.0.0.0', port=8080, debug=True)
