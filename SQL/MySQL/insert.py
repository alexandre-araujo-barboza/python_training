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

    # CUIDADO: ISSO LIMPA A TABELA
    cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

  # Começo a manipular dados a partir daqui
  with connection.cursor() as cursor:
    sql = (
      f'INSERT INTO {TABLE_NAME} '
       '(nome, idade) '
       'VALUES '
       '(%s, %s) '
    )
    data = ("Luiz", 18)
    result = cursor.execute(sql, data)
    print(sql, data)

    data = ("João", 42)
    result = cursor.execute(sql, data)
    print(sql, data)

    data = ("Sérgio", 18)
    result = cursor.execute(sql, data)
    print(sql, data)

    connection.commit()
