from flask import Flask
from flaskext.mysql import MySQL
mysql = MySQL()

def sanDb():
    """Database Connection."""
    app = Flask(__name__)
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
    app.config['MYSQL_DATABASE_DB'] = 'sandeep'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    return mysql
