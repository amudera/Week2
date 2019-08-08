#Basic SQL syntax

import sqlite3
from pprint import pprint

connection = sqlite3.connect("school.dtb")
cursor = connection.cursor()

def quit():
    global connection
    connection.commit()
    connection.close()

def SELECT():
    SQL = "SELECT * FROM coursaddes;"
    cursor.execute(SQL)
    cursor.fetchall() #will  all of the attributes of the data into a fetchall statement

def SELECT_WHERE():
    SQL = "SELECT * FROM courses WHERE pk=?;"
    cursor.execute(SQL,(1,))
    print(cursor.fetchone())

def INSEERT_INTO():
    SQL = "INSERT INTO courses(title,code,description) VALUES(?,?,?)"
    cursor.execute(SQL,('Theory of Computation','CS202','finite state machines'))

def UPDATE_WHERE():
    SQL = "UPDATE courses SET code='CS302' WHERE code ='CS202';"
    cursor.execute(SQL)
    
def DELETE_WHERE():
    SQL = "DELETE FROM courses WHERE title='Theory of Computation';"
    cursor.execute(SQL)

 if __name__ = "__main__":
        INSERT_INTO()
        SELECT_WHERE()
        print()
        UPDATE_WHERE()
        SELECT()
        print()
        DELETE_WHERE()
        SELECT()
        quit()

#if you dont have quote marks around a SQL command it will assume it is a table and throw you an error