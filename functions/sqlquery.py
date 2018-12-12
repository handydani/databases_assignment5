import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "flowers.db")
conn = sqlite3.connect(db_path)

# print(flowers_path)


# headers = ['genus','species','comname']
# data_table = pd.read_csv(flowers_path, header=None, names=headers, converters={'zip': str})
# print(data_table)
# if os.path.exists('example.db'):
#     os.remove('example.db')
print(db_path)


# data_table.to_sql('data_table', conn, dtype={
#     'genus':'VARCHAR(256)',
#     'species':'VARCHAR(256)',
#     'comname':'VARCHAR(256)',
# })

# print(data_table)
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

def sql_query3(query,num):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchmany(num)
    return rows

def sql_query_for_sightings(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchmany(10)
    return rows


name = "Draperia"
rows = sql_query_for_sightings('''SELECT * FROM SIGHTINGS WHERE NAME = ? ORDER BY SIGHTED DESC''', (name,))
for each in rows:
    print(each['name'], each['person'], each['location'], each['sighted'])