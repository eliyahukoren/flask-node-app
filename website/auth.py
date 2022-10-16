import re
from flask import Blueprint, render_template, request, flash

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
        try:
            check_sign_up_data()
        except ValueError as message:
            flash(str(message), category="error")
        else:
            flash('Account created', category="success")
    else:
        pass
    return render_template('sign_up.html')


def check_sign_up_data():
    """
    Simple check function.
    
    Check if all required fields on form is filled and have valid values
    
    return True on success and Exception on error
    """
    print(request.form)
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    if len(email) < 4:
        raise ValueError('Email must be greater than 3 characters.')
    
    if len(first_name) < 2:
        raise ValueError('First name must be greater than 1 character.')

    if password1 != password2:
        raise ValueError("Password don't match!")
    
    if len(password1) < 8:
        raise ValueError('Password must be at least 8 characters.')


def create_new_user():
    pass