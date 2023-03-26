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
dane = c.execute('SELECT * FROM user')
c.execute('INSERT INTO user (email,password_hash,name) VALUES ("kwp@tlen.pl","secret","Tomek")')
conn.commit()

print(dane.fetchall())