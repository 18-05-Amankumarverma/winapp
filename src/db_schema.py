import sqlite3

connection = sqlite3.connect('sql.db')
cursor = connection.cursor()
query  = """
    CREATE TABLE user(
        firstname varchar(30),
        lastname varchar(30),
        emailid varchar(100),
        phonenumber number(10)
    
    )
    
"""

cursor.execute(query)