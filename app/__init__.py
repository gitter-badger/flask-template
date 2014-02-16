from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
# from models import System, Subsystem, Parts, ServiceCall, WarrantyClaimForm
from flask.ext.basicauth import BasicAuth
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

mail = Mail(app)
basic_auth = BasicAuth(app)

from app import views, models