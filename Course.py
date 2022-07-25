import pickle


class Course:
    def __init__(self, course_id, course_name, course_credits, course_description):
        self.course_id = course_id
        self.course_name = course_name
        self.course_credits = course_credits
        self.course_description = course_description

    def get_professor_id(self):
        pass

    def add_course(self, course_info):
        # insert into Courses(course_info + professor_id)
        pass

    def assign_professor(self, professor_id):
        # insert into Courses(course_info + professor_id)
        pass


# Testing --> attempting to add data to the database
import psycopg2

first_course = Course(1, 'test', 300, 'test desc')
conn = psycopg2.connect(
    database="DB_WebStudent",
    user='postgres',
    password='postgres123',
    host='localhost',
    port=5432
)
cursor = conn.cursor()
script = 'SELECT * FROM courses'
cursor.execute(script)
print(cursor.fetchall())

try:
    conn = psycopg2.connect(
        database="DB_WebStudent",
        user='postgres',
        password='postgres123',
        host='localhost',
        port=5432
    )
    cursor = conn.cursor()
    script = 'INSERT INTO courses VALUES(%s,%s)'
    obj_string = pickle.dumps(first_course)

    rec_to_insert = ()

    # script = 'INSERT INTO Courses (name,description,professorId) VALUES("1","1",1)'
    # script = 'SELECT * FROM "DB_WebStudent".public.tables.UserTypes'
    cursor.execute('INSERT INTO courses VALUES(1,%s,%s)')
    print(cursor.fetchall())


except TimeoutError as error:
    print("Error! Please check database configuration!")

finally:
    if conn:
        conn.close()
    if cursor:
        cursor.close()
