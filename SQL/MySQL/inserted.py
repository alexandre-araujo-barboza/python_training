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
  
  with connection.cursor() as cursor:
        
    # Inserindo dados

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
    
    sql_many = (
      f'INSERT INTO {TABLE_NAME} '
       '(nome, idade) '
       'VALUES '
       '(%(name)s, %(age)s) '
    )

    data_many = (
      {"name": "Yoko", "age": 33},
      {"name": "Júlia", "age": 74},
      {"name": "Rose", "age": 53}
    )

    result = cursor.executemany(sql_many, data_many)
    
    print(sql_many, data_many)

    connection.commit()
