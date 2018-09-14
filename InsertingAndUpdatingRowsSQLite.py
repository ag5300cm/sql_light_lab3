
#Inserting and updating rows into an existing SQLite database table - next to sending queries - is
#probably the most common database operation. The Structured Query Language has a convenient
#UPSERT function, which is basically just a merge between UPDATE and INSERT: It inserts new rows
#into a database table with a value for the PRIMARY KEY column if it does not exist yet, or updates a row
#for an existing PRIMARY KEY value.Unfortunately, this convenient syntax is not supported by the more
#compact SQLite database implementation that we are using here. However, there are some
#workarounds. But let us first have a look at the example code

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_3'
id_column = 'my_1st_column'
column_name = 'my_2nd_column'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Inserts an ID with a specific value in a second column
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
#Both A) INSERT and B) INSERT OR IGNORE have in common that they append new rows to the
#database if a given PRIMARY KEY does not exist in the database table, yet. However, if we’d try to
#append a PRIMARY KEY value that is not unique, a simple INSERT would raise an
#sqlite3.IntegrityError exception, which can be either captured via a try-except statement (case A)
#or circumvented by the SQLite call INSERT OR IGNORE (case B). This can be pretty useful if we want to
#construct an UPSERT equivalent in SQLite. E.g., if we want to add a dataset to an existing database
#table that contains a mix between existing and new IDs for our PRIMARY KEY column.

# C) Updates the newly inserted or pre-existing entry
c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)".\
        format(tn=table_name, cn=column_name, idf=id_column))

conn.commit()
conn.close()