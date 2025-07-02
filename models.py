from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    proveedor = db.Column(db.String(100), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    remito = db.Column(db.String(50))
    factura = db.Column(db.String(50))
    estado = db.Column(db.String(30), nullable=False, default='pendiente')
