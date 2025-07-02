from flask import Flask, render_template, request, redirect, url_for
from models import db, Orden
from datetime import datetime
from sqlalchemy import or_
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ordenes_db_xr0d_user:ZCblVclkNhYxejHOnDXUbVm4hLDNnBHu@dpg-d1il1sre5dus73a1b8gg-a.ohio-postgres.render.com/ordenes_db_xr0d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Listados para dropdowns (ejemplo corto, completá con tu lista real)
proveedores = [
    "ABB SOCIEDAD ANONIMA",
    "ACERTUBO SOCIEDAD DE RESPONSABILIDAD LIMITADA",
    "ACOSTA MIGUEL ANGEL"
    # agregá todos los proveedores...
]

responsables = [
    "DANIEL LOPEZ",
    "GUARAZ JOAQUIN",
    "CHAVEZ MAXIMILIANO EMMANUEL"
    # agregá todos los responsables...
]

@app.route('/', methods=['GET'])
def index():
    search = request.args.get('search')
    if search:
        ordenes = Orden.query.filter(
            or_(
                Orden.numero_orden.ilike(f'%{search}%'),
                Orden.remito.ilike(f'%{search}%'),
                Orden.factura.ilike(f'%{search}%')
            )
        ).order_by(Orden.fecha.desc()).all()
    else:
        ordenes = Orden.query.order_by(Orden.fecha.desc()).all()
    return render_template('index.html', ordenes=ordenes, search=search)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nueva_orden = Orden(
            numero_orden=request.form.get('numero_orden'),
            numero_requerimiento=request.form.get('numero_requerimiento'),
            fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d'),
            proveedor=request.form['proveedor'],
            responsable=request.form['responsable'],
            remito=request.form.get('remito'),
            factura=request.form.get('factura'),
            estado=request.form.get('estado')
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', orden=None, proveedores=proveedores, responsables=responsables)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    orden = Orden.query.get_or_404(id)
    if request.method == 'POST':
        orden.numero_orden = request.form.get('numero_orden')
        orden.numero_requerimiento = request.form.get('numero_requerimiento')
        orden.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        orden.proveedor = request.form['proveedor']
        orden.responsable = request.form['responsable']
        orden.remito = request.form.get('remito')
        orden.factura = request.form.get('factura')
        orden.estado = request.form.get('estado')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', orden=orden, proveedores=proveedores, responsables=responsables)

if __name__ == '__main__':
    app.run(debug=True)

