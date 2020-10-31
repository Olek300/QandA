import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#above shows all avaliable tables
c.execute("SELECT * FROM QandAApp_qandamodel;")

print(c.fetchall())
conn.commit()
conn.close()
