from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField
import website.models as models

class CollegeForm(FlaskForm):
    college_code = StringField('College', [validators.DataRequired(), validators.Length(min=3, max=10)])
    college_name = StringField('College Description', [validators.DataRequired(), validators.Length(max=50)])
    submit = SubmitField("Save")
