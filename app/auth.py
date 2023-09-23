from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, request, redirect, url_for, render_template
from db import mysql


def register(app):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        hashed_password = generate_password_hash(password, method='sha256')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))
    return render_template('register.html')

def login(app):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['username'] = user['username']
            return redirect(url_for('contacts.Index'))
        else:
            return "Incorrect username or password"
    return render_template('login.html')
