import os
import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
  host = os.environ['MYSQL_HOST'],
  user = os.environ['MYSQL_USER'],
  password = os.environ['MYSQL_PASSWORD'],
  database = os.environ['MYSQL_DATABASE'],
  charset = 'utf8mb4'
)

with connection.cursor() as cursor:

  # Apagando com DELETE, WHERE e placeholders no PyMySQL
  
  sql = (
    f'DELETE FROM {TABLE_NAME} '
     'WHERE id = %s'
  )
  cursor.execute(sql, (1,))
  connection.commit()

  cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
  for row in cursor.fetchall():
    print(row)

  