import mysql.connector

def select_loginSQL(username, password):
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
        cursor.execute(f"select * from register where email='{username}' and password='{password}';")
        answer = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return answer
    except Exception as e:
        print(f"Login SQL Error {e}")