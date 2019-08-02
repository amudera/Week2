import sqlite3
import os

DIRPATH = os.path.dirname(__file__) 
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def teacher_for_course(coursename,dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.row
        cur = conn.cur()
    #tells you how to format the data you acquire, lets you use dictionary like syntax to index the data you get back
     
        SQL = """SELECT teachers.name 
        FROM teachers JOIN courses 
        ON teacher.pk=courses.teachers_pk;
        WHERE courses.name = ?;"""

        cur.execute(SQL,(coursename,))
        result = cur.fetchone()
        if not result:
            return None
        else:
            return result['name']

def students_for_teacher(teachername,dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cur()
        SQL = """SELECT students.name
            FROM teachers JOIN courses 
                ON teacher.pk=courses.teachers_pk;
                JOIN courses_students 
                ON courses.pk = courses_students.courses_pk
                JOIN students
                ON students.pk = courses_students.students.pk
            WHERE teachers.name = ?;"""
        cur.execute(SQL,(teachername,))
        results = cur.fetchall()
        return [result['name'] for result in results]

def students_for_course(coursename):

def courses_for_teacher(teachername):

def courses_for_studnent(studentname)

if __name__ == "__main__":
    # print(teacher_for_course("P.E."))
    print("Coach Gunn")