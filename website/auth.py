from flask import Blueprint,flash, render_template, request, redirect, url_for
from . import authmodule
from flask_login import login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        if authmodule.login():
            return redirect(url_for('views.home', user=current_user))
        else:
            flash('Wrong email or password, try again.', category='error')
        
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST' and authmodule.sign_up():
        return redirect(url_for('views.home', user=current_user))
                        
    return render_template('sign_up.html', user=current_user)

