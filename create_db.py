#!/usr/bin/address.py

import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

print("opened database successfully")

c.execute('''CREATE TABLE IF NOT EXISTS HASH 
        (personal_name, address, zip_code, phone_number)''')

# commit the changes to db
conn.commit()

# close the connection
conn.close()
