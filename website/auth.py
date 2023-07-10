from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        user = User.query.filter_by(email=form['email']).first()
        if user:
            equal_password = check_password_hash(user.password, form['password'])
            if equal_password: print('user found')
            else: print('wrong password')
        else: print('user not found')
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.form

        user = User.query.filter_by(email=form['email']).first()
        if not user:
            new_user = User(email=form['email'], first_name=form['name'], password=generate_password_hash(form['password'], method='sha256'))
            db.session.add(new_user)
            db.session.commit()
        else:
            print('user already registered with this email')
        
    return render_template('signup.html')