from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(16)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_blog import routes
