from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db792362d1434963fb710db181132774'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#this was not necessary to display the username
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from spice import routes