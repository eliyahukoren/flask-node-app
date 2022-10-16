import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        data = [email, first_name, password1, password2]

        try:
            
            check_sign_up_data(data=data)
            create_new_user(data=data)
            flash('Account created', category="success")
            return redirect(url_for('views.home'))
            
        except ValueError as message:
            print('error')
            flash(str(message), category="error")
            
    return render_template('sign_up.html')


def check_sign_up_data(data):
    """
    Simple check function.
    
    Check if all required fields on form is filled and have valid values
    
    return True on success and Exception on error
    """
    email, first_name, password1, password2 = data
    print(request.form)
    
    if len(email) < 4:
        raise ValueError('Email must be greater than 3 characters.')
    
    if len(first_name) < 2:
        raise ValueError('First name must be greater than 1 character.')

    if password1 != password2:
        raise ValueError("Password don't match!")
    
    if len(password1) < 8:
        raise ValueError('Password must be at least 8 characters.')
    
    return True


def create_new_user(data):
    email, first_name, password1, _ = data
    new_user = User(
        email=email, 
        first_name=first_name, 
        password=generate_password_hash(password1, method="sha256")
    )
    
    db.session.add(new_user)
    db.session.commit()