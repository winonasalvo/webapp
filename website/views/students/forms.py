from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import website.models as models

year_level = ('1st Year','2nd Year','3rd Year','4th Year')
gengen = ('Male','Female', 'Prefer not to Specify')

class StudentForm(FlaskForm):
    id = StringField('ID Number', [validators.DataRequired(), validators.Length(min=9, max=9)])
    fname = StringField('First Name', [validators.DataRequired(), validators.Length(max=50)])
    lname = StringField('Last Name', [validators.DataRequired(), validators.Length(max=50)])
    gender = SelectField('Gender', choices=gengen)
    year = SelectField('Year Level', choices= year_level)
    course = SelectField('Course', [validators.DataRequired(), validators.Length(max=50)])
    submit = SubmitField("Save")
