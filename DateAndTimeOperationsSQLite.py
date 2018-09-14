
#SQLite inherited the convenient date and time operations from SQL,
#  which are one of my favorite features of the Structured Query Language:
# It does not only allow us to insert dates and times in various different formats,
# but we can also perform simple + and - arithmetic, for example to look up entries
# that have been added xxx days ago

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'my_table_7'   # name of the table to be created
id_field = 'id' # name of the ID column
date_col = 'date' # name of the date column
time_col = 'time'# name of the time column
date_time_col = 'date_time' # name of the date & time column
field_type = 'TEXT'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({fn} {ft} PRIMARY KEY)'\
        .format(tn=table_name, fn=id_field, ft=field_type))

# A) Adding a new column to save date insert a row with the current date
# in the following format: YYYY-MM-DD
# e.g., 2014-03-06
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name, cn=date_col))
# insert a new row with the current date and time, e.g., 2014-03-06
c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES('some_id1', DATE('now'))"\
         .format(tn=table_name, idf=id_field, cn=date_col))

# B) Adding a new column to save date and time and update with the current time
# in the following format: HH:MM:SS
# e.g., 16:26:37
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name, cn=time_col))
# update row for the new current date and time column, e.g., 2014-03-06 16:26:37
c.execute("UPDATE {tn} SET {cn}=TIME('now') WHERE {idf}='some_id1'"\
         .format(tn=table_name, idf=id_field, cn=time_col))

# C) Adding a new column to save date and time and update with current date-time
# in the following format: YYYY-MM-DD HH:MM:SS
# e.g., 2014-03-06 16:26:37
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
         .format(tn=table_name, cn=date_time_col))
# update row for the new current date and time column, e.g., 2014-03-06 16:26:37
c.execute("UPDATE {tn} SET {cn}=(CURRENT_TIMESTAMP) WHERE {idf}='some_id1'"\
         .format(tn=table_name, idf=id_field, cn=date_time_col))

# The database should now look like this:
# id         date           time        date_time
# "some_id1" "2014-03-06"   "16:42:30"  "2014-03-06 16:42:30"

# 4) Retrieve all IDs of entries between 2 date_times
c.execute("SELECT {idf} FROM {tn} WHERE {cn} BETWEEN '2013-03-06 10:10:10' AND '2015-03-06 10:10:10'".\
    format(idf=id_field, tn=table_name, cn=date_time_col))
all_date_times = c.fetchall()
print('4) all entries between ~2013 - 2015:', all_date_times)

# 5) Retrieve all IDs of entries between that are older than 1 day and 12 hrs
c.execute("SELECT {idf} FROM {tn} WHERE DATE('now') - {dc} >= 1 AND DATE('now') - {tc} >= 12".\
    format(idf=id_field, tn=table_name, dc=date_col, tc=time_col))
all_1day12hrs_entries = c.fetchall()
print('5) entries older than 1 day:', all_1day12hrs_entries)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

#Some of the really convenient functions that return the current time and date are:

#DATE('now') # returns current date, e.g., 2014-03-06
#TIME('now') # returns current time, e.g., 10:10:10
#CURRENT_TIMESTAMP # returns current date and time, e.g., 2014-03-06 16:42:30

#  (or alternatively: DATETIME('now'))

#The screenshot below shows the print outputs of the code that we used to
# query for entries that lie between a specified date interval using

#BETWEEN '2013-03-06 10:10:10' AND '2015-03-06 10:10:10'

#and entries that are older than 1 day via

#WHERE DATE('now') - some_date
#Note that we don’t have to provide the complete time stamps here, the same syntax applies to simple dates or simple times only, too.\


