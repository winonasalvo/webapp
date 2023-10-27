from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import website.models as models

coll = ('CASS','CCS','CEBA','CHS', 'CSM', 'COE', 'CED')

class CourseForm(FlaskForm):
    course_code = StringField('Course', [validators.DataRequired(), validators.Length(min=3, max=10)])
    course_name = StringField('Course Description', [validators.DataRequired(), validators.Length(max=50)])
    college = SelectField('College', choices=coll)
    submit = SubmitField("Save")
