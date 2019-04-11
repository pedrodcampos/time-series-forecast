import mysql.connector
from .settings import (MYSQL_SERVER,
                       MYSQL_PORT,
                       MYSQL_USERNAME,
                       MYSQL_PASSWORD,
                       MYSQL_DATABASE)

mysqldb = mysql.connector.connect(
    host=MYSQL_SERVER,
    port=MYSQL_PORT,
    user=MYSQL_USERNAME,
    passwd=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
    raw=False
)
