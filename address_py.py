#!/usr/bin/python3

import sqlite3 

con = sqlite3.connect("test.db")

def main():
    answer = input("Press (1) to store, (2) to retrieve\n")
    print(answer)
    if answer == "1": # enter function to store data into Address Book
        #print("write to database")
        write_function()
    if answer == "2":  # access address boook
        #print("Read from database")
        read_function()

def write_function():
    try:
        cursor = con.cursor()
        personal_name = input("Name: ")
        address = input("Address Line: ")
        zip_code = int(input("Zip Code: "))
        phone_number = input("Phone #: ")
        data = (personal_name, address, zip_code, phone_number)
        query = ''' INSERT into HASH (personal_name, address, zip_code, phone_number) VALUES (?,?,?,?) '''
        cursor.execute(query, data)
        con.commit()
        if (cursor.execute(query,data)):
            print("Data Inserted Successfully")
        else:
            print("Data not Inserted")
        cursor.close()
    except:
        print("Database Error")
        con.close() # db close

def read_function(): # read DB
    try:
        cursor = con.cursor()
        select_data = 'SELECT * FROM HASH'
        cursor.execute(select_data)

        row = cursor.fetchall()
        print("Total rows are: ", len(row))
        print("Printing each row")
        for i in row:
            print("personal name: ", i[0])
            print("address: "       , i[1])
            print("zip code: "      , i[2])
            print(" phone number: ", i[3])
            print("\n")

        cursor.close()

    except:
        print("Error")

main()

