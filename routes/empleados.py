from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.empleado import Empleado
from utils.db import db

empleados = Blueprint('empleados',__name__)

@empleados.route("/")
def index():
    empleados = Empleado.query.all()
    return render_template('index.html', empleados = empleados)

@empleados.route('/crear', methods = ['POST'])
def crear():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    correo = request.form['correo']
    foto = request.form['foto']

    nuevo_empleado = Empleado(nombre, apellido, dni, correo, foto)

    db.session.add(nuevo_empleado)
    db.session.commit()

    flash("Empleado añadido satisfactoriamente!")

    return redirect(url_for('empleados.index'))

@empleados.route('/actualizar/<id>', methods = ['GET', 'POST'])
def actualizar(id):
    if request.method == 'POST':
        empleado = Empleado.query.get(id)
        empleado.nombre = request.form["nombre"]
        empleado.apellido = request.form["apellido"]
        empleado.dni = request.form["dni"]
        empleado.correo = request.form["correo"]
        empleado.foto = request.form["foto"]

        db.session.commit()

        flash("Empleado modificado satisfactoriamente!")

        return redirect(url_for("empleados.index"))
    
    empleado = Empleado.query.get(id)
    return render_template("actualizar.html", empleado = empleado)

@empleados.route('/eliminar/<id>')
def eliminar(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()

    flash("Empleado eliminado satisfactoriamente!")

    return redirect(url_for('empleados.index'))

@empleados.route('/about')
def about():
    return render_template('about.html')
