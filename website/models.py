from website import mysql

class Students(object):

    def __init__(self, id=None, fname=None, lname=None, gender=None, year=None, course=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.year = year
        self.course = course

    def add(self):
        curs = mysql.cursor()

        sql = f"INSERT INTO data(id,fname,lname,gender,year,course) \
                VALUES('{self.id}','{self.fname}','{self.lname}','{self.gender}','{self.year}','{self.course}')" 

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
    def edit(cls, idnumber):
        curs = mysql.cursor()
        sql = f"SELECT * from data where STUDENTID = {idnumber}" 
        curs.execute(sql)
        id = curs.fetchall()
        return id

    @classmethod
    def update(cls, id):
        try:
            curs = mysql.cursor()
            sql = f"UPDATE from data where STUDENTID= {id}"
            curs.execute(sql)
            mysql.commit()
            return True
        except:
            return False

    @classmethod
    def delete(cls,id):
        try:
            curs = mysql.cursor()
            sql = f"DELETE from users where id= {id}"
            curs.execute(sql)
            mysql.commit()
            return True
        except:
            return False
        

class Courses(object):

    def __init__(self, course_code=None, course_name=None):
        self.course_code = course_code
        self.course_name = course_name

    def add(self):
        cursor = mysql.cursor()

        sql = f"INSERT INTO course(course_code,course_name) \
                VALUES('{self.course_code}','{self.course_name}')" 

        cursor.execute(sql)
        mysql.commit()
    @classmethod
    def all(cls):
        cursor = mysql.cursor()

        sql = f"SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def populate(cls):
        curs = mysql.cursor()
        sql = "SELECT COURSEID FROM course"
        curs.execute(sql)
        result = [item[0] for item in curs.fetchall()]
        return result


