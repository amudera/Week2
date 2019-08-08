import sqlite3
import os

DIRPATH = os.path.dirname(__file__) 
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def seed(dbpath):

with sqlite3.connect(dbpath) as conn:
    cur = conn.cur()

    SQL = """INSERT INTO courses (name,teachers_pk) VALUES (?,?);"""
    for course in courses:
        cur.execute(SQL,course)

     SQL = """INSERT INTO teachers (name) VALUES (?);"""
    for teacher in teachers:
        cur.execute(SQL,teacher)

     SQL = """INSERT INTO students (name) VALUES (?);"""
    for student in students:
        cur.execute(SQL,student)

     SQL = """INSERT INTO courses_students VALUES (?,?);"""
    for course_student in courses_students:
        cur.execute(SQL,course_student)

if __name__ == "__main__":
    schema(dbpath)