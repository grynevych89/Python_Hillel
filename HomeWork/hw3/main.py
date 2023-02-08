from flask import Flask, request
from utils import execute_sql

app = Flask(__name__)


# http://127.0.0.1:5001/phones/create?phone_value=380952159175&contact_name=Nick
@app.route("/phones/create")
def phones_create():
    phone_value = request.args['phone_value']
    contact_name = request.args['contact_name']

    sql = f'''
    INSERT INTO Phones (PhoneValue, ContactName)
    VALUES ('{phone_value}', '{contact_name}');
    '''
    execute_sql(sql)
    return ''


# http://127.0.0.1:5001/phones/read
@app.route("/phones/read")
def phones_read():
    import sqlite3
    con = sqlite3.connect("phones.db")
    cur = con.cursor()

    sql = '''
        SELECT * FROM Phones;
        '''
    res = cur.execute(sql)
    phones = res.fetchall()
    con.close()
    return phones


# http://127.0.0.1:5001/phones/update?phone_id=1&contact_name=Igor&phone_value=095215999
@app.route("/phones/update")
def phones_update():
    phone_id = request.args['phone_id']
    contact_name = request.args['contact_name']
    phone_value = request.args['phone_value']
    sql = f'''
    UPDATE Phones
    SET ContactName = '{contact_name}',
        PhoneValue = '{phone_value}'
    WHERE PhoneID = {phone_id};
    '''
    execute_sql(sql)
    return ''


# http://127.0.0.1:5001/phones/delete?phone_id=1
@app.route("/phones/delete")
def phones_delete():
    phone_id = request.args['phone_id']
    sql = f'''
    DELETE FROM Phones
    WHERE PhoneID = {phone_id};
    '''
    execute_sql(sql)
    return ''


if __name__ == '__main__':
    app.run(debug=True, port=5001)
