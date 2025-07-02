from app import app, db

with app.app_context():
    db.drop_all()    # Borra todas las tablas (pierdes datos)
    db.create_all()  # Crea las tablas nuevas con las modificaciones
print("Migración completada")
