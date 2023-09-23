from flask import Flask

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

from db import mysql

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    from auth import register
    return register(app)

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    from auth import login
    return login(app)



