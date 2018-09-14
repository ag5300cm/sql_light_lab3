

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'my_table_3'   # name of the table to be created
id_column = 'my_1st_column' # name of the PRIMARY KEY column
new_column1 = 'my_2nd_column'  # name of the new column
new_column2 = 'my_3nd_column'  # name of the new column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'Hello World' # a default value for the new column rows

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))
#We just added 2 more columns (my_2nd_column and my_3rd_column) to my_table_2 of our SQLite
#database next to the PRIMARY KEY column my_1st_column.
#The difference between the two new columns is that we initialized my_3rd_column with a default value
#(here:’Hello World’), which will be inserted for every existing cell under this column and for every new
#row that we are going to add to the table if we don’t insert or update it with a different value.

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()