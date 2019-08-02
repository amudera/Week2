#!/usr/bin/env python3
import csv
import sqlite3

with open('employees.csv','r') as f:
    data = f.readlines()
    for lines in data:
        data2 = lines.split()

def upload_all(dbname="newdatabase.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        SQL = """CREATE TABLE everything (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR,
            last_name VARCHAR,
            cellphone VARCHAR,
            homephone VARCHAR,
            workphone VARCHAR,
            email VARCHAR,
            country VARCHAR
        );"""

        cur.execute(SQL)
        add_data = 

def create_numbers(dbname="newdatabase.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        NUMS = """CREATE TABLE numbers (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR,
            last_name VARCHAR,
            cellphone VARCHAR,
            homephone VARCHAR,
            workphone VARCHAR
        );"""

        cur.execute(NUMS)

def create_users(dbname="newdatabase.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        
        USERS = """CREATE TABLE users (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR,
            country VARCHAR
        );"""
        
        cur.execute(USERS)

def insert_data1(dbname="newdatabase.db",data2):
     with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        for row in data2:
            value = "INSERT INTO numbers SELECT (first_name,last_name,cellphone,homephone,workphone) VALUES (?,?,?,?,?) FROM everything"
            cur.execute(value)
            cur.fetchall()


def insert_data2(dbname="newdatabase.db",data2):
     with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        for row in data2:
            value2 = "INSERT INTO users SELECT (first_name,last_name,email,country) VALUES (?,?,?,?) FROM everything"
            cur.execute(value2)
            cur.fetchall()

def input(dbname="newdatabase.db"):
     with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        aspect = input("What aspect would you like to query? ")
        select = input("Which attribute would you like to query? ")
        SQL2 = "'SELECT * FROM users WHERE '{}' = '{}'".format(aspect,select)
        cur.execute(SQL2)

input()