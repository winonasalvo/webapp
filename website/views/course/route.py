from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import mysql
import website.models as models
from website.views.students.forms import StudentForm

course = Blueprint('course', __name__)

@course.route('/courses')
def course_page():
    courses = models.Courses.all()
    print(courses)
    return render_template('courses/courses.html', course = courses)

"""
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

    #print(data.id)
    if request.method == 'POST' and form.validate():
        students = models.Students(id = form.id.data, fname=form.fname.data, lname=form.lname.data, gender=form.gender.data, year= form.year.data, course=form.course.data)
        print("students", students)
        print(data[0]['id'])
        print(students.fname)
        students.update(id) 
        print("students added")
        
        flash("Update Success!")
        return redirect('/')
 
    else:
        print("else")
        return render_template('students/edit_students_data.html', form = form)

@student.route('/delete_student/<id>', methods=['POST'])
def delete_row(id):
    form = StudentForm()
    print(id)
    data = models.Students.delete(id)

    flash('Delete Success!')
    print("flash")
    return redirect('/')
    if data == True:
        flash('Delete Success!')
    else:
        flash('Delete was not successful.')
    
"""