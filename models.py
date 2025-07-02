from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_orden = db.Column(db.String(50), nullable=True)
    numero_requerimiento = db.Column(db.String(50), nullable=True)  # <-- esta línea
    fecha = db.Column(db.Date, nullable=False)
    proveedor = db.Column(db.String(100), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    remito = db.Column(db.String(50))
    factura = db.Column(db.String(50))
    estado = db.Column(db.String(20))