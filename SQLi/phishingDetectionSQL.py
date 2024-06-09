import mysql.connector

def insert_phishingDetectionSQL(url):
    try:
        db = {
            "host": "127.0.0.1",
            "port": 8889,
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
            "user": "root",
            "password": "root",
            "database": "ultron",
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**db)
        cursor = connection.cursor()
        cursor.execute(f"INSERT into phishingDetectionSQL VALUES('{url}');")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Phishing Detection SQL Error {e}")

def select_phishingDetectionSQL():
    try:
        db = {
            "host": "127.0.0.1",
            "port": 8889,
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
            "user": "root",
            "password": "root",
            "database": "ultron",
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**db)
        cursor = connection.cursor()
        cursor.execute(f"select * from phishingDetectionSQL;")
        answer = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return answer
    except Exception as e:
        print(f"Phishing Detection SQL Error {e}")