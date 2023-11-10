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

@course.route('/courses/view_students/<course_code>')
def course_view_page(course_code):
    courses = models.Students.fetch(course_code)

    return render_template('students/students.html', student = courses)


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

    #print(data.id)
    if request.method == 'POST' and form.validate():
        courses = models.Courses(course_code=form.course_code.data, course_name=form.course_name.data, college=form.college.data)
        print("courses", courses)

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
    
@course.route('/course/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        result = models.Courses()
        print("field", field)
        print("result", result)
        

        if field == 'select':
            result = result.search(keyword=user_input)
        elif field == 'course':
            result = result.search(keyword=user_input, field='course')
        elif field == 'name':
            result = result.search(keyword=user_input, field='name')
        elif field == 'college':
            result = result.search(keyword=user_input, field='college')
        else:
            result = []

        print(str(len([result])))
        if result != None:
            courses = result
            return render_template('/courses/courses.html', course = courses)
        else:
            flash(f'No student found', 'info')
            return render_template('/courses/courses.html')
    else:
        return redirect(url_for('course.courses'))
