from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import mysql
import website.models as models
from website.views.college.forms import CollegeForm

college = Blueprint('college', __name__)

@college.route('/colleges')
def college_page():
    colleges = models.Colleges.all()
    print(colleges)
    return render_template('colleges/colleges.html', colleges = colleges)

@college.route('/colleges/view_students/<college_code>')
def course_view_page(college_code):
    course = models.Colleges.fetch(college_code)
    print(course)
    print(college_code)

    return render_template('students/students.html', student = course)

@college.route('/data_colleges', methods=['POST','GET'])
def data_colleges_page():
    form = CollegeForm()
    if request.method == 'POST' and form.validate(): 
        colleges = models.Colleges(college_code = form.college_code.data, college_name = form.college_name.data)      
        colleges.add() 
        return redirect('/colleges')
    
    else:
        return render_template('colleges/data_colleges.html', form = form)

     
@college.route('/edit_college/<college_code>', methods=['GET','POST'])
def edit_college_page(college_code):
    form = CollegeForm()

    #print(data.id)
    if request.method == 'POST' and form.validate():
        colleges = models.Colleges(college_code = form.college_code.data, college_name = form.college_name.data)
        colleges.update(college_code) 
        
        flash("Update Success!")
        return redirect('/colleges')
 
    else:
        print("else")
        return render_template('colleges/edit_colleges_data.html', form = form)

@college.route('/delete_college/<college_code>', methods=['POST'])
def delete_row(college_code):
    form = CollegeForm()
    data = models.Colleges.delete(college_code)

    flash('Delete Success!')
    print("flash")
    return redirect('/colleges')
    if data == True:
        flash('Delete Success!')
    else:
        flash('Delete was not successful.')
    
