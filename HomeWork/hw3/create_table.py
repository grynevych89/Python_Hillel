import sqlite3
con = sqlite3.connect('phones.db')
cur = con.cursor()

sql = '''
CREATE TABLE Phones (
    PhoneID INTEGER PRIMARY KEY,
    PhoneValue varchar(255),
    ContactName varchar(255)
);
'''
cur.execute(sql)
con.commit()
con.close()
