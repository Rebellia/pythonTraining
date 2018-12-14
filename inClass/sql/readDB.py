#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('gameinv.db')
print('opened db connection')

cursor = conn.execute ("SELECT id, name, publisher, smokedam, desc, price from PCGAMES")

for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("PUB = ", row[2])
    print("SMOKE = ", row[3])
    print("DESC = ", row[4])
    print("PRICE = ", row[5])







