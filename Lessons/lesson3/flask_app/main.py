from flask import Flask, request
from utils import generate_passwords

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length_str = request.args.get('length', '10')
    if not length_str.isdigit():
        return 'Length should be a digit'

    length = int(length_str)

    if length <= 0:
        return 'Length should be positive'

    if length > 1000:
        return 'Password is too long'

    return generate_passwords(length)


@app.route("/emails/create")
def emails_create():
    import sqlite3
    con = sqlite3.connect('tutorial.db')
    cur = con.cursor()

    sql = '''
    INSERT INTO Emails (EmailValue, Name)
    VALUES ('test@asd.com', 'John');
    '''
    cur.execute(sql)
    con.commit()
    con.close()
    return ""


@app.route("/emails/read")
def emails_read():
    import sqlite3
    con = sqlite3.connect('tutorial.db')
    cur = con.cursor()

    sql = '''
    SELECT * FROM Emails;
    '''
    # res =
    cur.execute(sql)
    con.commit()
    con.close()
    return ""


@app.route("/emails/update")
def emails_update():
    import sqlite3
    con = sqlite3.connect('tutorial.db')
    cur = con.cursor()

    sql = '''
    UPDATE Emails
    SET name = '{name}'
    WHERE EmailID = {email_id};
    '''
    # res =
    cur.execute(sql)
    con.commit()
    con.close()
    return ""


@app.route("/emails/delete")
def emails_delete():
    import sqlite3
    con = sqlite3.connect('tutorial.db')
    cur = con.cursor()

    sql = '''
    DELETE * FROM Emails;
    '''
    # res =
    cur.execute(sql)
    con.commit()
    con.close()
    return ""


if __name__ == '__main__':
    app.run()
