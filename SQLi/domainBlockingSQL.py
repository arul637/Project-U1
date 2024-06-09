import mysql.connector

def insert_domainBlockingSQL(domain):
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
        cursor.execute(f"INSERT into domainBlockingSQL VALUES('{domain}');")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"domain Blocking SQL Error {e}")

def select_domainBlockingSQL():
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
        cursor.execute(f"select * from domainBlockingSQL;")
        answer = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return answer
    except Exception as e:
        print(f"domain Blocking SQL Error {e}")

def delete_domainBlockingSQL(domain):
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
        cursor.execute(f"delete from domainBlockingSQL where domain='{domain}';")
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"domain Blocking SQL Error {e}")