import sqlite3
con = sqlite3.connect('tutorial.db')
cur = con.cursor()

sql = '''
CREATE TABLE Emails (
    EmailID INTEGER PRIMARY KEY,
    EmailValue varchar(255),
    Name varchar(255)
);
'''
cur.execute(sql)
con.commit()
con.close()