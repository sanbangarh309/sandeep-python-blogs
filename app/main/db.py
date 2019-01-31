from flask import Flask
from flaskext.mysql import MySQL
from flask_pymongo import PyMongo,MongoClient
mysql = MySQL()
mongo = PyMongo()
client = MongoClient()

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

def sanMongoDb():
    """Database Connection."""
    app = Flask(__name__)
    # MongoDb configurations
    app.config["MONGO_URI"] = "mongodb://sandeep_blog_user:sandy12345@ds261114.mlab.com:61114/sandeep_blogs"
    client = MongoClient('mongodb://sandeep_blog_user:sandy12345@ds261114.mlab.com:61114/sandeep_blogs')
    db = client.sandeep_blogs
    # result = db.users.find()
    # for document in result:
    #     print(document)
    # mongo = PyMongo(app)
    # mongo.init_app(app)
    return db
