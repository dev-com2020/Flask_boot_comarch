import sqlite3
conn = sqlite3.connect('blog.db')
c = conn.cursor()
dane = c.execute('SELECT * FROM tag')
# c.execute('INSERT INTO tag (name,slug) VALUES ("C++","c++")')
# conn.commit()

print(dane.fetchall())