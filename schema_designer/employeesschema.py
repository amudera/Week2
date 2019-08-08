import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "employees.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)


def schema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS employees;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE employees(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            SSN VARCHAR(9),
            salary INTEGER,
            phone TEXT,
            FOREIGN KEY(employees_pk) REFERENCES employees(pk)
            );"""
        cursor.execute(SQL)

        SQL = "DROP TABLE IF EXISTS departments;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE departments(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            DepID VARCHAR(128),
            Name TEXT,
            Budget FLOAT,
            FOREIGN KEY(dept_pk) REFERENCES departments(pk)
        );"""
        cursor.execute(SQL)

        SQL = """DROP TABLE IF EXISTS dept_employees;"""
        cursor.execute(SQL)

        SQL = """CREATE TABLE dept_employees(
            employees_pk
            dept_pk,
            FOREIGN KEY(employees_pk) REFERENCES employees(pk),
            FOREIGN KEY(dept_pk) REFERENCES departments(pk),
            UNIQUE(employees_pk, dept_pk)
        );"""
        cursor.execute(SQL)

if __name__ == "__main__":
    schema(DBPATH)