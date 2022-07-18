from flask import Flask
from routes.empleados import empleados
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cpsuslcweyrunu:b03118e111f21d08259fa3a7e7de2817a470463d9fb9aa5a9ef3e7b25a8f13db@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d87mnd5vinkjc7'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(empleados)
