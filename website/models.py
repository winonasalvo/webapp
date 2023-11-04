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

    """
    @classmethod
    def edit(cls, id):
        curs = mysql.cursor()
        sql = f"SELECT * from student WHERE `id` = '{id}'" 
        curs.execute(sql)
        id = curs.fetchall()
        return id """

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
        print("search: ", students)
        if field is None: 
            result = self.search_by_field(students, keyword, 'all')
        elif field == 'id':
            result = self.search_by_field(students, keyword, 'id')
        elif field == 'firstname':
            result = self.search_by_field(students, keyword, 'firstname')
        elif field == 'lastname':
            result = self.search_by_field(students, keyword, 'lastname')
        elif field == 'gender':
            result = self.search_by_field(students, keyword, 'gender')
        elif field == 'year':
            result = self.search_by_field(students, keyword, 'year')
        elif field == 'course':
            result = self.search_by_field(students, keyword, 'course')
        
        return result

    @staticmethod
    def search_by_field(rows: list = None, keyword: str = None, field: str = None) -> list:
        result = []
        for row in rows:
            row_allcaps = [str(cell).upper() for cell in row]

            if field == 'all':
                if keyword in row_allcaps:
                    result.append(row)
            elif field == 'id':
                if keyword == row_allcaps[0]:
                    result.append(row)
                    return result
            elif field == 'firstname':
                if keyword == row_allcaps[1]:
                    result.append(row)
            elif field == 'lastname':
                if keyword == row_allcaps[2]:
                    result.append(row)
            elif field == 'gender':
                if keyword == row_allcaps[3]:
                    result.append(row)
            elif field == 'year':
                if keyword == row_allcaps[4]:
                    result.append(row)
            elif field == 'course':
                print('course', keyword, row_allcaps[5])
                if keyword == row_allcaps[5]:
                    result.append(row)

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

    @classmethod
    def all(cls):
        cursor = mysql.cursor()

        sql = f"SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def edit(cls, course_code):
        curs = mysql.cursor()
        sql = f"SELECT * from course WHERE `course_code` = '{course_code}'" 
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
        


    @classmethod
    def all(cls):
        cursor = mysql.cursor()

        sql = f"SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result