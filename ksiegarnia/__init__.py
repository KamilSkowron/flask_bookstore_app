from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)

api = Api(app)

from ksiegarnia import routes



