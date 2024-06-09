import mysql.connector

def insert_passwordManagerSQL(website, username, password, description):
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
        cursor.execute(f"INSERT into passwordManagerSQL VALUES('{website}', '{username}', '{password}', '{description}');")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"password Manager SQL Error {e}")

def select_passwordManagerSQL():
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
        cursor.execute(f"select * from passwordManagerSQL;")
        answer = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return answer
    except Exception as e:
        print(f"password Manager SQL Error {e}")

def delete_passwordManagerSQL(website):
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
        cursor.execute(f"delete from passwordManagerSQL where website='{website}';")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"password Manager SQL Error {e}")
