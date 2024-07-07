import os
import dotenv
import pymysql
import pymysql.cursors
TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
  host = os.environ['MYSQL_HOST'],
  user = os.environ['MYSQL_USER'],
  password = os.environ['MYSQL_PASSWORD'],
  database = os.environ['MYSQL_DATABASE'],
  charset = 'utf8mb4',
  cursorclass = pymysql.cursors.DictCursor,
)

with connection.cursor() as cursor:
  
  # Trocando o cursor para retornar dicionários
  # pymysql.cursors.DictCursor

  cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
  for row in cursor.fetchall():
    print(row)
