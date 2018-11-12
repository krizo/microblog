from app import app
from flask import render_template, redirect, flash, url_for

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'kriz'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(url_for('index'), title='Home', user=user, posts=posts)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)
