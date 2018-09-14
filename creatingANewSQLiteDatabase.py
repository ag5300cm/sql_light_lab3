

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_3'  # name of the table to be created
table_name2 = 'my_table_4'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


#Tip:
#A handy tool to visualize and access SQLite databases is the free FireFox SQLite Manager
#https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/?src

#Here is a quick overview of all data types that are supported by SQLite 3:
#   INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
#   REAL: An 8-byte floating point value.
#   TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
#   BLOB: A blob of data (binary large object) for storing binary data.
#   NULL: A NULL value, represents missing data or an empty cell.