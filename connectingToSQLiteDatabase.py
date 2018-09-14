

# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html


#where the database file (sqlite_file) can reside anywhere on our disk, e.g.,
sqlite_file = 'test.db'
#In general, the only thing that needs to be done before we can perform any operation on a SQLite
#database via Python’s sqlite3 module, is to open a connection to an SQLite database file:
import sqlite3
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#And if we performed any operation on the database other than sending queries, we need to commit
#those changes via the .commit() method before we close the connection:
conn.commit()  # we didn't do anything so don't need

#If we are finished with our operations on the database file,
#we have to close the connection via the .close() method:
conn.close()