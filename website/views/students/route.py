from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import mysql
import website.models as models
from website.views.students.forms import StudentForm

student = Blueprint('student', __name__)

@student.route('/')
def students_page():
    students = models.Students.all()
    print(students)
    return render_template('students/students.html', student = students)

@student.route('/data_students', methods=['POST','GET'])
def data_students_page():
    form = StudentForm()
    print(form.id)
    print("form added")
    if request.method == 'POST' and form.validate(): 
        students = models.Students(id = form.id.data, fname=form.fname.data, lname=form.lname.data, gender=form.gender.data, year= form.year.data, course=form.course.data)
        #form.course.choices = [(models.Courses.populate())]  
        print(students)      
        students.add() 
        print("students added")
        return redirect('/')
    
    else:
        return render_template('students/data_students.html', form = form)
    
@student.route('/edit_students/<id>', methods=['GET','POST'])
def edit_students_page(id):
    form = StudentForm()
    data = models.Students.edit(id)
    print(data)
    if request.method == 'POST' and form.validate():
        data.id = request.form['id']
        data.fname = request.form['fname']
        data.lname = request.form['lname']
        data.gender = request.form['gender']
        data.year = request.form['year']
        data.course = request.form['course']
        """try:
            flash("Update Success!")
            print(data)
            return render_template("students/edit_students_data.html", form = form, data = data)
        except:
            flash("Update Success!")
            print(data)
            return render_template("students/edit_students_data.html", form = form, data = data)"""
    else:
        print("else")
        return render_template('students/edit_students_data.html', form = form)