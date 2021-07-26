from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    username = StringField('Full Name ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    contact = IntegerField('Contact', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    pincode = IntegerField('Pincode', validators=[DataRequired()])
    bloodgroup = SelectField('Blood Group', choices=[('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), (
        'ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[
                        ('m', 'MALE'), ('f', 'FEMALE')], validators=[DataRequired()])
    lastdonation = DateField('Last donation date', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Full Name ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remembeer Me')
    submit = SubmitField('Sign In')
