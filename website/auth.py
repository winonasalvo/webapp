from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        id = request.form.get('id')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')

        if len(id) != 9:
            flash('Enter correct ID No.', category='error')
        elif len(year) != 1:
            flash('Enter correct year', category='error')
        else:
            #add user to database
            flash('Account created!', category="success")
            
    return render_template("sign_up.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")