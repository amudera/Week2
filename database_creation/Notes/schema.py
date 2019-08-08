import sqlite3
import os

DIRPATH = os.path.dirname(__file__) #takes the file path to your directory where this file is in
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def schema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cur()
        SQL = "DROP TABLE IF EXISTS courses;" #if it exists drop it, if it doesnt the dont give an error
        cur.execute(SQL)

        SQL = """CREATE TABLE courses(
            pk INTERGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(64),
            teachers_pk INTEGER, 
            FOREIGN KEY(teachers_pk) REFERENCES teachers(pk)
        );"""
        cur.execute(SQL)

#in this table one of the attributes will be a key that references entires in another table, will reference integer primary key
#in the teachers table

        SQL = "DROP TABLE IF EXISTS teachers;" #if it exists drop it, if it doesnt the dont give an error
        cur.execute(SQL)

        SQL = """CREATE TABLE teachers(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128),
            );"""
        
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS students;" #if it exists drop it, if it doesnt the dont give an error
        cur.execute(SQL)

        SQL = """CREATE TABLE students(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128),
            );"""
        
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS courses_students;" 
        cur.execute(SQL)

        SQL = """CREATE TABLE courses_students(
            courses_pk,
            students_pk,
            FOREIGN KEY(courses_pk) REFERENCES courses(pk),
            FOREIGN KEY(students_pk) REFERENCES students(pk),
            UNIQUE(courses_pk,students_pk)
            );"""

        cur.execute(SQL)
#courses pk is a reference to pk in the courses table

  if __name__ == "__main__":
        schema(DBPATH)
