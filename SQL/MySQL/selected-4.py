import os
from typing import cast
import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
  host = os.environ['MYSQL_HOST'],
  user = os.environ['MYSQL_USER'],
  password = os.environ['MYSQL_PASSWORD'],
  database = os.environ['MYSQL_DATABASE'],
  charset = 'utf8mb4',
  cursorclass = CURRENT_CURSOR,
)

dotenv.load_dotenv()

with connection.cursor() as cursor:
  
  # Detalhes de consultas executadas
  # rowcount, rownumber e lastrowid para 

  cursor.execute(
    f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
  )
  lastIdFromSelect = cursor.fetchone()
  resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

  data = cursor.fetchall()
  for row in data:
    print(row)

  print('result from select:', resultFromSelect)
  print('len:', len(data))
  print('row count:', cursor.rowcount)
  print('last row id:', cursor.lastrowid)
  print('last row id from select:', lastIdFromSelect)

  cursor.scroll(0, 'absolute')
  print('row number', cursor.rownumber)
