import sqlite3
import os
from pprint import pprint

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "sitemetrics.db"
DBPATH = os.path.join(DIRNAME, DBFILENAME)

def query():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    aspect = input("What aspect would you like to query? ")
    select = input("Which attribute would you like to query? ")
    SQL = "SELECT COUNT(*) FROM search_terms WHERE {} = '{}';".format(aspect,select)
    cur.execute(SQL)
    results = cur.fetchall()
    pprint(results)
    quit()


def querymax():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT * FROM users WHERE page_views = (SELECT MIN(page_views) FROM users);"
    cur.execute(SQL)
    results = cur.fetchall()
    pprint(results)
    quit()

def queryfirst():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT * FROM users WHERE id=1;"
    cur.execute(SQL)
    results = cur.fetchall()
    print(results)
    quit()

def querymax():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT id FROM user_searches WHERE term_id = 'drain';"
    results = cur.fetchall()
    pprint(results)
    quit()

def queryid():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT * FROM user_searches WHERE id = '391';"
    results = cur.fetchall()
    pprint(results)
    quit()

querymax()

# def query2():
#     connection = sqlite3.connect(DBPATH)
#     cur = connection.cursor()
#     select = input("Which attribute would you like to query? ")
#     cur.execute('SELECT * FROM users WHERE state=?',(select,))
#     results = cur.fetchall()
#     pprint(count(results)
#     quit()

# query2()


def partial():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    aspect = input("What aspect would you like to query? ")
    select = input("Which attribute would you like to query? ")
    SQL3 = "SELECT * FROM users WHERE {} LIKE '%{}%';".format(aspect,select)
    cur.execute(SQL3)
    results = cur.fetchall()
    pprint(results)

def orderby():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT city FROM users WHERE city LIKE 'V%' ORDER BY city ASC;"
    cur.execute(SQL)
    results = cur.fetchall()
    pprint(results)
    quit()

def query():
    connection = sqlite3.connect(DBPATH)
    cur = connection.cursor()
    SQL = "SELECT * FROM user_searches WHERE last_visit = '2014-08-22';".format(aspect,select)
    cur.execute(SQL)
    results = cur.fetchall()
    pprint(results)
    quit()

if __name__ == "__main__":
    query()