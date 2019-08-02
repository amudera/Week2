#programatically add data to a database e.g when migrating data from once source to another
#testing data
#kind of like run once and then delete

import sqlite3

def seed(dbname="school.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        SQL = """DELETE FROM courses;""" #delete all the data in courses. 
        cur.execute(SQL)

        SQL = """INSERT INTO courses(title,code,description) VALUES(?, ?, ?);""" #dont need to specify pk again if the database already exists
        #if the table name "courses" doesnt exist this will throw up an error
        #the values method uses ? referencing the SQL built in support to ensure we dont execute any sql keywords that come into the statement
        courses = [
            ("Comp Sci","CS101","earn to code"),
            ("Literature","LIT101","reading stuff")
        ]

        # for course in courses:
        #     cur.execute(SQL,(value1,value2,value3))
        
        
        for course in courses:
            cur.execute(SQL,course)

    if __name__ = "__main__":
        seed()

    SELECT * FROM courses; #will return everything in that database