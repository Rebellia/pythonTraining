#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('gameinv.db')
print("Opened DB successfully!")

conn.execute("INSERT INTO PCGAMES (ID, NAME,PUBLISHER,SMOKEDAM, DESC,PRICE) VALUES(2, 'Blizzard', 'Random', 0, 'first person shooter', 200.00)")

conn.commit()

print("Records created successfully")
conn.close()
