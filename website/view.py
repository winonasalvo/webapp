from flask import Blueprint, render_template
from website import mysql
import website.models as models

view = Blueprint('views', __name__)

@view.route('/home')
def home():
    students = models.Students.all()
    print(students)
    return render_template('students/students.html', student = students)
