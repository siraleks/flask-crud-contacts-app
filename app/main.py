from flask import Flask
from flask_migrate import Migrate
from db import db
from app import app
from contacts import contacts
from auth import auth

# Die Blueprints registrieren
app.register_blueprint(contacts)
app.register_blueprint(auth)

# Die Datenbank mit der App initialisieren
db.init_app(app)

# Flask-Migrate initialisieren
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=3000, debug=True)




