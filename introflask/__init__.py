from flask import Flask, request, session, g, redirect, url_for, abort, \render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b9af53f1a776b80268cff4bf12d46cf3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinook.db'
app.config['SQLALCHEMY_BINDS'] = { 'two' :'sqlite:///site.db'}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from introflask import routes
