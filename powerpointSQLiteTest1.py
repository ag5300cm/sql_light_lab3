
try:
    __author__ = '?'
    import sqlite3

    conn = sqlite3.connect("test.db")

    print("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY3
        (ID INT PRIMARY KEY  NOT NULL,
        NAME        TEXT    NOT NULL,
        AGE         INT     NOT NULL,
        ADDRESS     CHAR(50),
        SALARY      REAL);''')
    print("Table created successsfully")

    conn.close()
except ConnectionError:
    print("Table could already be made...? ")
    print(ConnectionError)
