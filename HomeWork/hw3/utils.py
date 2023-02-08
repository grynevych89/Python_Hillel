def execute_sql(sql: str) -> None:
    import sqlite3
    con = sqlite3.connect("phones.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
