# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# print(connection)
# print(cur)
# connection.close()
# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()
import sqlite3

conn = sqlite3.connect('weather.db')
cur = connection.cursor()
cur.execute("CREATE TABLE temperature (date_time TEXT, temperature REAL)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-01 10:00', 23.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-02 11:00', 24.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-03 12:00', 25.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-04 13:00', 26.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-05 14:00', 27.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-06 15:00', 28.5)")
cur.execute("INSERT INTO temperature VALUES ('2020-04-07 16:00', 29.5)")
conn.commit()
cur.execute("SELECT * FROM temperature WHERE date_time > datetime('now', '-7 days')")
print(c.fetchall())
conn.close()