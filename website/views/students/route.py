from flask import Blueprint, render_template
from website import mysql
import website.models as models


student = Blueprint('student', __name__)

@student.route('/')
def home():
    students = models.Students.all()
    print(students)
    return render_template('students/students.html', student = students)
