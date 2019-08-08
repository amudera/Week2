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