import sqlite3
import os

DIRPATH = os.path.dirname(__file__) 
DBPATH = os.path.join(DIRPATH,DBFILENAME)

def snackschema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cur = conn.cur()
        SQL = "DROP TABLE IF EXISTS snacks;"
        cur.execute(SQL)

        SQL = """CREATE TABLE snacks(
            pk INTERGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Type TEXT,
            PRICE FLOAT,
            QUANTITY INTEGER,
        );"""
        cur.execute(SQL)