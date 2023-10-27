from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import mysql
import website.models as models
from website.views.course.forms import CourseForm

course = Blueprint('course', __name__)

@course.route('/courses')
def course_page():
    courses = models.Courses.all()
    print(courses)
    return render_template('courses/courses.html', course = courses)

@course.route('/data_courses', methods=['POST','GET'])
def data_courses_page():
    form = CourseForm()
    print(form.course_code)
    print("form added")
    if request.method == 'POST' and form.validate(): 
        courses = models.Courses(course_code=form.course_code.data, course_name=form.course_name.data, college=form.college.data)
        #form.course.choices = [(models.Courses.populate())]  
        print(courses)      
        courses.add() 
        print("courses added")
        return redirect('/courses')
    
    else:
        return render_template('courses/data_courses.html', form = form)

  
@course.route('/edit_course/<course_code>', methods=['GET','POST'])
def edit_courses_page(course_code):
    form = CourseForm()
    data = models.Courses.edit(course_code)
    
    print(data)

    #print(data.id)
    if request.method == 'POST' and form.validate():
        courses = models.Courses(course_code=form.course_code.data, course_name=form.course_name.data, college=form.college.data)
        print("courses", courses)
        print(data[0]['course_code'])

        courses.update(course_code) 
        
        flash("Update Success!")
        return redirect('/courses')
 
    else:
        print("else")
        return render_template('courses/edit_courses_data.html', form = form)

@course.route('/delete_course/<course_code>', methods=['POST'])
def delete_course_row(course_code):
    form = CourseForm()
    print(course_code)
    data = models.Courses.delete_course(course_code)
    print(data)
    data = models.Courses.delete(course_code)

    if data == True:
        flash('Delete Success!')
        print("flash")
        return redirect('/courses')
        
    else:
        flash('Delete was not successful.')
        return redirect('/data_courses')
