#!/usr/bin/env python3

import sqlite3

#will be created if doesn't exist
conn = sqlite3.connect('gameinv.db')
print("Opened DB successfully")

conn.execute('''CREATE TABLE PCGAMES
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
PUBLISHER TEXT NOT NULL,
SMOKEDAM BOOL NOT NULL,
DESC CHAR(50),
PRICE REAL);''')

print("Table created successfully")
conn.close()
