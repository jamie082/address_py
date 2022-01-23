#!/usr/bin/python3

import sqlite3

# http://tutorialspoint.com/sqlite/sqlite_python.htm

def main():
    answer = input("Press (1) to store, (2) to retrieve\n")
    print(answer)
    if answer == "1": # enter function to store data into Address Book
        print("write to database")
        write_function()
    if answer == "2":  # access address boook
        print("Read from database")
        read_function()

def write_function():
    try:
        sqliteConnection = sqlite.connect('test.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_insert_query)
        sqlteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            print("Total Rows affected since the database connection was opened: ")
            sqliteConnection.close()
            print("sqlite connection is closed")

def read_function(): # read DB
    try:
        sqliteConnection = sqlite.connect('test.db') # connect to db
    except: # if error (db is not read)
        print("Error reading DB")

main()
