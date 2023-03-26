# import sqlite3
# conn = sqlite3.connect('_blog.db')
# c = conn.cursor()
# dane = c.execute('SELECT * FROM tag')
# # c.execute('INSERT INTO tag (name,slug) VALUES ("C++","c++")')
# # conn.commit()
#
# print(dane.fetchall())


import sqlite3
conn = sqlite3.connect('_blog.db')
c = conn.cursor()
dane = c.execute('SELECT * FROM entry')
c.execute('INSERT INTO entry (title,slug,content,status) VALUES ("Kod dla C++","kod-dl-c++","Kod dla C++...", 1)')
conn.commit()

print(dane.fetchall())