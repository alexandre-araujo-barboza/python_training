import os
from typing import cast
import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.SSDictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
  host = os.environ['MYSQL_HOST'],
  user = os.environ['MYSQL_USER'],
  password = os.environ['MYSQL_PASSWORD'],
  database = os.environ['MYSQL_DATABASE'],
  charset = 'utf8mb4',
  cursorclass = CURRENT_CURSOR,
)

# para conjuntos de dados muito grandes
# SSCursor, SSDictCursor e scroll

with connection.cursor() as cursor:
  cursor = cast(CURRENT_CURSOR, cursor)
  cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
  cursor.scroll(2)
  for row in cursor.fetchall_unbuffered():
    print(row)
    if row['id'] >= 5:
      break
