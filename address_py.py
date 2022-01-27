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
        personal_name = input("Name: ")
        address = input("Address Line: ")
        zip_code = input("Zip Code: ")
        phone_number = input("Phone #: ")

        data = (personal_name, address, zip_code)
        data = ''' (personal_name, address, zip_code, phone_number) VALUES (?,?,?,?) '''
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
        # Something else went wrong
            print("sqlite connection is closed")

    con.close() # db close

def read_function(): # read DB
    try:
        sqliteConnection = sqlite3.connection('test.db')   
        print("Connected to Sqlite")
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor = sqliteConnection.cursor()
        print("List of tables\n")
    except: # if error (db is not read)
        print("Error reading DB")

    con.close()

main()
