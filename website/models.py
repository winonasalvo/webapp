from flask import flash
from website import mysql
import pymysql

def check_id_format(id_number):
    if len(id_number) != 9:
        raise ValueError("Size")
    if not (str(id_number[:4]).isdigit() and str(id_number[5:]).isdigit()):
        raise ValueError("Error")
    if id_number[:4] != str(range(2017,2024)):
        raise ValueError("Wrong Id")

    
class Students(object):

    def __init__(self, id=None, fname=None, lname=None, gender=None, year=None, course=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.year = year
        self.course = course

    def add(self):
        try:
            curs = mysql.cursor()

            sql = f"INSERT INTO student (`id`, `fname`, `lname`, `course`, `year`, `gender`) VALUES('{self.id}', '{self.fname}', '{self.lname}', '{self.course}', '{self.year}', '{self.gender}')"
            check_id_format(self.id)
            
            curs.execute(sql)
            mysql.commit()

        except pymysql.err.Error:
            # Handle exception
            flash("Error: Student's course not in course list", 'error')
        except ValueError as e:
            if str(e) == "Size":
                flash("Error: Input correct ID size", 'error')
            if str(e) == "Error":
                flash("Error: Input correct ID format", 'error')
            if str(e) == "Wrong Id":
                flash("Error: Input appropriate ID number(year-XXXX)", "error")
            
        

    def update(self, id):
        curs = mysql.cursor()
        sql = f''' UPDATE student
            SET 
                id = '{self.id}', 
                fname = '{self.fname}', 
                lname = '{self.lname}', 
                course = '{self.course}',
                year = '{self.year}', 
                gender = '{self.gender}' WHERE id = '{id}'; '''
        print(sql)
        curs.execute(sql)
        mysql.commit()

    @classmethod
    def all(cls):
        curs = mysql.cursor()
        sql = curs.execute("SELECT * from student")
        if sql > 0:
            result = curs.fetchall()
        return result


    @classmethod
    def fetch(cls, course_code):
        curs = mysql.cursor()
        sql = f"SELECT * from student WHERE `course` = '{course_code}'" 
        curs.execute(sql)
        result = curs.fetchall()
        return result 

    @classmethod
    def delete(cls,id):
        try:
            curs = mysql.cursor()
            sql = f"DELETE from student where `id`= '{id}'"
            curs.execute(sql)
            mysql.commit()
            return True
        except:
            return False
        
    
    def search(self, keyword: str = None, field: str = None):
        keyword = keyword.upper()
        students = self.all()
        result = []
        print("keyword", keyword)
        if field is None: 
            result = self.search_by_field(students, keyword, 'all')
        elif field == 'id':
            result = self.search_by_field(students, keyword, 'id')
        elif field == 'fname':
            result = self.search_by_field(students, keyword, 'fname')
        elif field == 'lname':
            result = self.search_by_field(students, keyword, 'lname')
        elif field == 'gender':
            result = self.search_by_field(students, keyword, 'gender')
        elif field == 'year':
            result = self.search_by_field(students, keyword, 'year')
        elif field == 'course':
            result = self.search_by_field(students, keyword, 'course')
        
        print("result2", result)
        return result

    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row = {key: value.upper() for key, value in row.items()}
            print('row1', row)
            if field == 'all':
                for key, value in row.items():
                    if keyword == value:
                        result.append(row)
            elif field == 'id':
                if keyword == row['id']:
                    result.append(row)
            elif field == 'fname':
                if keyword == row['fname']:
                    result.append(row)
            elif field == 'lname':
                if keyword == row['lname']:
                    result.append(row)
            elif field == 'gender':
                if keyword == row['gender'] or 'F':
                    result.append(row)
                if keyword == row['gender'] or 'M':
                    result.append(row)
            elif field == 'year':
                if keyword == row['year']:
                    result.append(row)
            elif field == 'course':
                print('course', keyword, row['course'])
                if keyword == row['course']:
                    result.append(row)

        print(result)
        return result


        

class Courses(object):

    def __init__(self, course_code=None, course_name=None, college=None):
        self.course_code = course_code
        self.course_name = course_name
        self.college = college

    def add(self):
        cursor = mysql.cursor()

        sql = f"INSERT INTO course(`course_code`,`course_name`, `college`) \
                VALUES('{self.course_code}','{self.course_name}', '{self.college}')" 

        cursor.execute(sql)
        mysql.commit()

    def update(self, course_code):
        curs = mysql.cursor()
        sql = f''' UPDATE course
            SET 
                course_code = '{self.course_code}', 
                course_name = '{self.course_name}', 
                college = '{self.college}' WHERE `course_code` = '{course_code}'; '''
        print(sql)
        curs.execute(sql)
        mysql.commit()

    def search(self, keyword: str = None, field: str = None):
        keyword = keyword.upper()
        students = self.all()
        result = []
        print("keyword", keyword)
        if field is None: 
            result = self.search_by_field(students, keyword, 'all')
        elif field == 'course':
            result = self.search_by_field(students, keyword, 'course')
        elif field == 'name':
            result = self.search_by_field(students, keyword, 'name')
        elif field == 'college':
            result = self.search_by_field(students, keyword, 'college')

        print("result2", result)
        return result

    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row = {key: value.upper() for key, value in row.items()}
            print('row1', row)
            if field == 'all':
                for key, value in row.items():
                    if keyword == value:
                        result.append(row)
            elif field == 'course':
                if keyword == row['course_code']:
                    result.append(row)
            elif field == 'name':
                if keyword == row['course_name']:
                    result.append(row)
            elif field == 'college':
                if keyword == row['college']:
                    result.append(row)
        print(result)
        return result
    
    @classmethod
    def all(cls):
        cursor = mysql.cursor()

        sql = f"SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def fetch(cls, college):
        curs = mysql.cursor()
        sql = f"SELECT * from course WHERE `college` = '{college}'" 
        curs.execute(sql)
        code = curs.fetchall()
        return code
    
    @classmethod
    def delete(cls,id):
            curs = mysql.cursor()
            sql = f" DELETE from course where `course_code`= '{id}'"
            print("course",id)
            print(sql)
            curs.execute(sql)
            mysql.commit()
            
            return True
    
    @classmethod
    def delete_course(cls,id):
        curs = mysql.cursor()
        sql = f"DELETE from student where `course`='{id}'"
        curs.execute(sql)
        mysql.commit()
        return True
    
    @classmethod
    def populate(cls):
        curs = mysql.cursor()
        sql = "SELECT COURSEID FROM course"
        curs.execute(sql)
        result = [item[0] for item in curs.fetchall()]
        return result

class Colleges(object):
    def __init__(self, college_code=None, college_name=None):
        self.college_code = college_code
        self.college_name = college_name
        
    def add(self):
        cursor = mysql.cursor()

        sql = f"INSERT INTO college(`college_code`,`college_name`) \
                VALUES('{self.college_code}','{self.college_name}')" 

        print(sql)
        cursor.execute(sql)
        mysql.commit()

    def update(self, college_code):
        curs = mysql.cursor()
        sql = f''' UPDATE college
            SET 
                college_code = '{self.college_code}', 
                college_name = '{self.college_name}' WHERE `college_code` = '{college_code}'; '''
        print(sql)
        curs.execute(sql)
        mysql.commit()

    @classmethod
    def all(cls):
        cursor = mysql.cursor()

        sql = f"SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def fetch(cls, college_code):
        curs = mysql.cursor()
        sql = f"SELECT * FROM student WHERE course IN (SELECT course_code FROM course WHERE college='{college_code}')" 
        print(sql)
        curs.execute(sql)
        code = curs.fetchall()
        return code
    
    @classmethod
    def delete(cls,college):
            curs = mysql.cursor()
            sql = f" DELETE from college where `college_code`= '{college}'"
            curs.execute(sql)
            mysql.commit()
            
            return True
    
    @classmethod
    def delete_course(cls,id):
        curs = mysql.cursor()
        sql = f"DELETE from student where `course`='{id}'"
        curs.execute(sql)
        mysql.commit()
        return True