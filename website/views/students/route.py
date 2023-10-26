from flask import Blueprint, render_template, request, flash, redirect
from website import mysql
import website.models as models
from website.views.students.forms import StudentForm

student = Blueprint('student', __name__)

@student.route('/')
def students_page():
    students = models.Students.all()
    print(students)
    return render_template('students/students.html', student = students)

@student.route('/data_students', methods = ['POST','GET'])
def data_students_page():
    form = StudentForm()
    if request.method == 'POST' and form.validate():
        students = models.Students(id = form.id, fname=form.fname, lname= form.lname, gender=form.gender, year= form.year, course=form.course)
        #form.course.choices = [(models.Courses.populate())]
        students.add()
        return redirect('/')
    else:
        return render_template('students/data_students.html', form = form)
    