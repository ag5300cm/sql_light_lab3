
__author__ = '?'
import sqlite3
conn = sqlite3.connect('test.db')
print("connection successful")

cursor = conn.execute("SELECT id, name, address,salary from "
                      "COMPANY3")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()