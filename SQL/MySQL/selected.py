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
with connection:
  with connection.cursor() as cursor:
        
    # Lendo os valores com SELECT
  
    menor = int(input('Digite a menor idade: '))
    maior = int(input('Digite a maior idade: '))
    
    sql = (
      f'SELECT * FROM {TABLE_NAME} '
       'WHERE idade BETWEEN %s AND %s  '
    )
    
    cursor.execute(sql, (menor, maior))
    print(cursor.mogrify(sql, (menor, maior)))
    data = cursor.fetchall()
    
    for row in data:
      print(row)
