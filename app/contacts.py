from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db import db
from models import Contact

contacts = Blueprint('contacts', __name__, template_folder='templates')

@contacts.route('/')
def index():
    # Alle Kontakte abfragen
    all_contacts = Contact.query.all()
    return render_template('index.html', contacts=all_contacts)


# ... [Previous code]

@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        new_contact = Contact(fullname=fullname, phone=phone, email=email)

        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact added successfully')
        except:
            flash('Error adding the contact')

    return redirect(url_for('contacts.index'))


@contacts.route('/edit/<id>')
def get_contact(id):
    contact = Contact.query.get(id)
    return render_template('edit-contact.html', contact=contact)


@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        contact = Contact.query.get(id)
        contact.fullname = request.form['fullname']
        contact.phone = request.form['phone']
        contact.email = request.form['email']

        try:
            db.session.commit()
            flash('Contact updated successfully')
        except:
            flash('Error updating the contact')

    return redirect(url_for('contacts.index'))


@contacts.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)

    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully')
    except:
        flash('Error deleting the contact')

    return redirect(url_for('contacts.index'))
