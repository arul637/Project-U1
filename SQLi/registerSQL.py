import mysql.connector

def insert_registerSQL(firstname, lastname, email, password):
    try:
        db = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "arulkumaran",
            "password": "ak21042004",
            "database": "ultron",
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**db)
        cursor = connection.cursor()
        cursor.execute(f"INSERT into register values('{firstname}', '{lastname}', '{email}', '{password}');")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Register SQL Error {e}")