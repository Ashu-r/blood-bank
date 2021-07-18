from flask.helpers import url_for
from app.forms import LoginForm, RegistrationForm
from flask import render_template , redirect , flash
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created ')
        return redirect(url_for('login'))
    return render_template('registration.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('login.html',form=form)
