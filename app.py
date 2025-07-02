from flask import Flask, render_template, request, redirect, url_for
from models import db, Orden
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ordenes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    ordenes = Orden.query.order_by(Orden.fecha.desc()).all()
    return render_template('index.html', ordenes=ordenes)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nueva_orden = Orden(
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
    return render_template('form.html', orden=None)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    orden = Orden.query.get_or_404(id)
    if request.method == 'POST':
        orden.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        orden.proveedor = request.form['proveedor']
        orden.responsable = request.form['responsable']
        orden.remito = request.form.get('remito')
        orden.factura = request.form.get('factura')
        orden.estado = request.form.get('estado')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', orden=orden)

if __name__ == '__main__':
    app.run(debug=True)
