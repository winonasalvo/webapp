from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import mysql
import website.models as models
from website.views.students.forms import StudentForm

student = Blueprint('student', __name__)

@student.route('/')
def students_page():
    students =  models.Students.all()
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
    
    if request.method == 'POST' and form.validate():
        students = models.Students(id = form.id.data, fname=form.fname.data, lname=form.lname.data, gender=form.gender.data, year= form.year.data, course=form.course.data)
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

    students = models.Students(id = form.id.data, fname=form.fname.data, lname=form.lname.data, gender=form.gender.data, year= form.year.data, course=form.course.data)
    students.delete(id)
    flash('Delete Success!')
    print("flash")
    return redirect('/')
    if data == True:
        flash('Delete Success!')
    else:
        flash('Delete was not successful.')
    
@student.route('/students/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        result = models.Students()
        print("field", field)
        print("result", result)
        

        if field == 'select':
            result = result.search(keyword=user_input)
        elif field == 'id':
            result = result.search(keyword=user_input, field='id')
        elif field == 'first':
            result = result.search(keyword=user_input, field='fname')
        elif field == 'last':
            result = result.search(keyword=user_input, field='lname')
        elif field == 'gender':
            result = result.search(keyword=user_input, field='gender')
        elif field == 'year':
            result = result.search(keyword=user_input, field='year')
        elif field == 'course':
            result = result.search(keyword=user_input, field='course')
        else:
            result = []

        print(str(len([result])))
        if result != None:
            student = result
            return render_template('/students/students.html', student = student)
        else:
            flash(f'No student found', 'info')
            return render_template('/students/students.html')
    else:
        return redirect(url_for('student.students'))

