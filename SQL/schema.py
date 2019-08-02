import sqlite3

#Definte database with tabular data

def create_table(dbname="school.db"):
    with sqlite3.connect(dbname) as conn: #creates a databas connection
        cur = conn.cursor()
        SQL = """DROP TABLE IF EXISTS courses;""" #drop table = delete a specific table. 
        #SQL words need to be in all caps to differentiate whats related to the data structure
        #SQL needs to end every single query in a semicolon as an end of command character

        cur.execute(SQL) #will take in the string and send it to SQL

        SQL = """CREATE TABLE courses (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128),
            code VARCHAR(6),
            description TEXT 
        );"""
         cur.execute(SQL)
    
    if __name__ == "__main__":
        create_table()

        #autoincrement means that you dont have to make unique pk's
        #varchar = string and brackets required if they need to fit an exact number of characters
        #TEXT doesnt have a specific number of characters