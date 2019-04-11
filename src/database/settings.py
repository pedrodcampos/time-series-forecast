from os import environ

MYSQL_SERVER = environ.get('MYSQL_SERVER', 'localhost')
MYSQL_PORT = environ.get('MYSQL_PORT', 3306)
MYSQL_DATABASE = environ.get('MYSQL_DATABASE', '')
MYSQL_USERNAME = environ.get('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD', '')
