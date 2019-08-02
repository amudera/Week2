import csv
import sqlite3
import os
from pprint import pprint

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "accounts.db"
CSVFILENAME = "employees.csv"
DBPATH = os.path.join(DIRNAME, DBFILENAME)

def seed_from_csv(csvpath, dbpath):
    with open(csvpath, 'r') as csvfile, sqlite3.connect(dbpath) as connection:
        reader = csv.DictReader(csvfile)
        curs = connection.cursor()

        curs.execute("""DELETE FROM people;""")

        for line in reader:
            SQL = """INSERT INTO people(
                name,
                email,
                country) VALUES (?, ?, ?);"""

            data = (line['name'], line['email'],
                    line['country'])

            curs.execute("""DELETE FROM numbers;""")

            SQL2 = """INSERT INTO numbers(
                name,
                cellphone,
                homephone,
                workphone) VALUES (?, ?, ?,?);"""

            data2 = (line['name'], line['cellphone'],
                    line['homephone'],line['workphone'])
            
            curs.execute(SQL, data)
            curs.execute(SQL2,data2)

def query():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    aspect = input("What aspect would you like to query? ")
    select = input("Which attribute would you like to query? ")
    SQL3 = "SELECT * FROM people WHERE {} = '{}';".format(aspect,select)
    cur.execute(SQL3)
    results = cur.fetchall()
    pprint(results)


def partial():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    aspect = input("What aspect would you like to query? ")
    select = input("Which attribute would you like to query? ")
    SQL3 = "SELECT * FROM people WHERE {} LIKE '%{}%';".format(aspect,select)
    cur.execute(SQL3)
    results = cur.fetchall()
    pprint(results)


partial()

if __name__ == "__main__":
    seed_from_csv(CSVPATH, DBPATH)
