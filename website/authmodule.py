from flask import request, flash
from flask_login import current_user, login_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


MIN_EMAIL_LENGTH = 4
WRONG_EMAIL_LENGTH_MSG = 'Email must be greater than 3 characters.'

MIN_PASSWORD_LENGTH = 4
WRONG_PASSWORD_LENGTH_MSG = f'Password must be at least {MIN_PASSWORD_LENGTH} characters.'
WRONG_PASSWORD_MATCH_MSG = 'Password don\'t match.'

MIN_FIRST_NAME_LENGTH = 2
WRONG_FNAME_LENGTH_MESSAGE = f'First name must be greater than {MIN_FIRST_NAME_LENGTH - 1} character.'

USER_ALREADY_EXIST_MESSAGE = 'User already exists.'

SUCCESS_SIGNUP_MESSAGE = 'Account created.'
SUCCESS_LOGIN_MESSAGE = 'Logged in successfully!'


def get_user_from_request():
    return User.query.filter_by(email=request.form.get('email')).first()


def login():
    if is_user_exists(
        email=request.form.get('email'),
        check_password=True,
        password=request.form.get('password')
    ):
        login_user(get_user_from_request(), remember=True)
        flash(SUCCESS_LOGIN_MESSAGE, category='success')
        return True
    else:
        return False
    
def sign_up():
    try:
        data = get_form_data()
        check_sign_up_data(data=data)
        create_new_user(data=data)
        flash(SUCCESS_SIGNUP_MESSAGE, category="success")
        login_user(get_user_from_request(), remember=True)
        return True
    except ValueError as message:
        flash(str(message), category="error")
        return False


def get_form_data():
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    return [email, first_name, password1, password2]


def check_sign_up_data(data):
    """
    Simple check function.
    
    Check if all required fields on form is filled and have valid values
    
    return True on success and Exception on error
    """
    email, first_name, password1, password2 = data


    if is_user_exists(email):
        raise ValueError(USER_ALREADY_EXIST_MESSAGE)

    if len(email) < MIN_EMAIL_LENGTH:
        raise ValueError(WRONG_EMAIL_LENGTH_MSG)

    if len(first_name) < MIN_FIRST_NAME_LENGTH:
        raise ValueError(WRONG_FNAME_LENGTH_MESSAGE)

    if password1 != password2:
        raise ValueError(WRONG_PASSWORD_MATCH_MSG)

    if len(password1) < MIN_PASSWORD_LENGTH:
        raise ValueError(WRONG_PASSWORD_LENGTH_MSG)

    

    return True


def is_user_exists(email, check_password=False, password=''):
    exist = False
    user = User.query.filter_by(email=email).first()
    
    if user:
        exist = True

        if check_password:
            exist = check_password_hash(pwhash=user.password, password=password)
    
    return exist


def create_new_user(data):
    email, first_name, password1, _ = data
    new_user = User(
        email=email,
        first_name=first_name,
        password=generate_password_hash(password1, method="sha256")
    )

    db.session.add(new_user)
    db.session.commit()
