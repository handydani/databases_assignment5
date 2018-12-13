import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "flowers.db")
conn = sqlite3.connect(db_path)

print(db_path)

conn.row_factory = sqlite3.Row

def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows

def sql_query3(query,var,num):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchmany(num)
    return rows

def sql_query_for_sightings(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchmany(10)
    return rows

