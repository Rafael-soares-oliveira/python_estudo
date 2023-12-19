import pymysql
import dotenv
import os
import pymysql.cursors

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

tab1 = ('CREATE TABLE IF NOT EXISTS CUSTOMERS ('
        'ID INT NOT NULL AUTO_INCREMENT, '
        'NOME VARCHAR(60) NOT NULL, '
        'IDADE INT NOT NULL, '
        'PRIMARY KEY (ID)'
        ')'
        )

with connection:
    with connection.cursor() as cursor:
        cursor.execute(tab1)
        connection.commit()
        print(cursor)
