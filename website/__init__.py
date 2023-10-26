from flask import Flask
import pymysql
import pymysql.cursors

mysql = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='student_database',
                             #charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_app():
    app  = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from .view import view
    from .auth import auth
    from .views.students.route import student

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(student, url_prefix='/')
    
    return app