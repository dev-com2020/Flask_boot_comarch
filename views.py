from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user

from app import app
from entries.forms import LoginForm


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            login_user(form.user, remember=form.remember_me.data)
            flash('Logged in successfully.')
            return redirect(request.args.get('next') or url_for('homepage'))
    else:
        form = LoginForm()

    return render_template('login.html', form=form)
