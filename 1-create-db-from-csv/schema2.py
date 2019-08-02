import sqlite3
import os
#this just creates the database
#when you create a table the schema has to have the exact same headers if youre doing a csv seed, if you dont put the headers exactly it will
#kick out an error

BASEDIR = os.path.dirname(__file__)
DBFILENAME = "employees.db"
DBPATH = os.path.join(BASEDIR, DBFILENAME)


def db_schema(database_path):
    with sqlite3.connect(database_path) as connection:
        curs = connection.cursor()
        curs.execute("""
            DROP TABLE IF EXISTS people;""")

        curs.execute("""
            CREATE TABLE people(
                name TEXT,
                email TEXT,
                country TEXT
            );""")
        
        curs.execute("""
            DROP TABLE IF EXISTS numbers;""")

        curs.execute("""
            CREATE TABLE numbers(
                name TEXT,
                homephone INT,
                cellphone INT,
                workphone INT
            );""")



if __name__ == "__main__":
    db_schema(DBPATH)
