import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)


def teacher_for_course(coursename, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT teachers.name
        FROM teachers JOIN courses
        ON teachers.pk = courses.teachers_pk
        WHERE courses.name = ?;"""

        cursor.execute(SQL, (coursename,))
        result = cursor.fetchone()
        if not result:
            return None
        else:
            return result['name']

def students_for_teacher(teachername, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT students.name
            FROM teachers JOIN courses
                ON teachers.pk = courses.teachers_pk
                    JOIN courses_students
                ON courses.pk = courses_students.courses_pk
                    JOIN students
                ON students.pk = courses_students.students_pk
            WHERE teachers.name = ?; """
        cursor.execute(SQL, (teachername,))
        results = cursor.fetchall()

        return [result['name'] for result in results]

def students_for_course(coursename, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT students.name
        FROM students JOIN courses
        ON students.pk = courses.students_pk
        WHERE courses.name = ?;"""

        cursor.execute(SQL, (coursename,))
        result = cursor.fetchone()
        if not result:
            return None
        else:
            return result['name']
        

def courses_for_teacher(teachername, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT course.name
        FROM courses JOIN teachers
        ON teachers.pk = courses.teachers_pk
        WHERE teachers.name = ?;"""

        cursor.execute(SQL, (teachername,))
        result = cursor.fetchone()
        if not result:
            return None
        else:
            return result['courses']

def courses_for_student(studentname, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT course.name
        FROM courses JOIN students
        ON students.pk = courses.students_pk
        WHERE students.name = ?;"""

        cursor.execute(SQL, (studentname,))
        result = cursor.fetchone()
        if not result:
            return None
        else:
            return result['courses']

if __name__=="__main__":
    # print(teacher_for_course("P.E."))
    print(students_for_teacher("Dr. Weaver"))