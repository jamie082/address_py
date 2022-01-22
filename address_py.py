#!/usr/bin/python3

from sqlite3 import connect

db = connect ('test.db')

answer = input("Press (1) to store, (2) to retrieve\n")
print(answer)

if answer == "1": # enter function to store data into Address Book
    store_var()
if answer == "2":  # access address boook
    write_db()

    try:
        cursor.execute(sqlite_insert_query(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as erorr:
        print("Erorr while working with SQLite", errorr)
    finally
        if sqliteConnection:
            print("Total Rows affected since the database connection was opened: ")
            sqliteConnection.close()
            print("sqlite connection is closed")

def write_db():
    
db.close()
