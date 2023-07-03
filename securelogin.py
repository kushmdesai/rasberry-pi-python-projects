import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
        id INTEGER PRIMARY KEY,
        username varchar(255) not null,
        password varchar(255) not null
)
""")
            
username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest() 
username2, password2 = "jhon", hashlib.sha256("mycatisgreat777".encode()).hexdigest()
username3, password3 = "striker999", hashlib.sha256("IlikeStrikeInG".encode()).hexdigest()
username4, password4 = "nuralnine", hashlib.sha256("nuralpassword".encode()).hexdigest()
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username1, password1))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username2, password2))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username3, password3))
cur.execute("INSERT INTO userdata(username,password) VALUES (?,?)",(username4, password4))

conn.commit