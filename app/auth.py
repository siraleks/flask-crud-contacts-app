from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from models import User

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new User instance
        new_user = User(username=username, password=hashed_password, email=email)

        try:
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            # If there's any issue, flash the error and redirect back to the registration page
            flash(str(e))
            return redirect(url_for('auth.register'))

    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Den Benutzer basierend auf dem angegebenen Benutzernamen abfragen
        user = User.query.filter_by(username=username).first()

        # Überprüfen, ob der Benutzer existiert und das Passwort korrekt ist
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('contacts.index'))
        else:
            flash('Login failed. Check your username and/or password.')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

