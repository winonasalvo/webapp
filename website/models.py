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

        sql = f"INSERT INTO student (`id`, `fname`, `lname`, `course`, `year`, `gender`) VALUES('{self.id}', '{self.fname}', '{self.lname}', '{self.course}', '{self.year}', '{self.gender}')"

        curs.execute(sql)
        mysql.commit()

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
    def edit(cls, id):
        curs = mysql.cursor()
        sql = f"SELECT * from student WHERE `id` = '{id}'" 
        curs.execute(sql)
        id = curs.fetchall()
        return id

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



