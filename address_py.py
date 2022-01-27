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
        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        name = input("First name: ")
        address = input("Address Line: ")
        zip_code = int(input("Zip Code: ")

        # Address Book
        # state = input("State: ")
        # http://pythonlobby.com/inserting-data-into-database-in-python-using-sqlite

        query = "INSERT into USERS (name, address, zip_code) VALUES (?,?,?)"
        data = (name, address, zip_code)
        cursor.execute(query, data)
        con.commit()
        if (cursor.execute(query,data)):
            print("Data Inserted Successfully")
        else:
            print("Data not Inserted")
        cursor.close()
    except:
        print("Database Error")
    finally:
        # print("Something Else Went Wrong")
        if sqliteConnection:
            print("Total Rows affected since the database connection was opened: ")
            sqliteConnection.close()
            print("sqlite connection is closed")

    con.close() # db close

def read_function(): # read DB
    # sqlite3 update
    try:
        con = sqlite3.connect('test.db')
    except: # if error (db is not read)
        print("Error reading DB")

    con.close()

main()
