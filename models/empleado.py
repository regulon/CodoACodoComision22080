from flask_sqlalchemy import SQLAlchemy
from utils.db import db

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id=db.Column(db.INT, primary_key=True)
    nombre=db.Column(db.VARCHAR(250), nullable=False)
    apellido=db.Column(db.VARCHAR(250), nullable=False)
    dni=db.Column(db.INT, nullable=False)
    correo=db.Column(db.VARCHAR(250), nullable=False, unique=True)
    foto=db.Column(db.VARCHAR(5000), nullable=False)
    

    def __init__(self, nombre, apellido, dni, correo, foto):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo
        self.foto = foto