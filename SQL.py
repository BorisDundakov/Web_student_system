import psycopg2


def connect():
    conn = None
    cursor = None

    conn = psycopg2.connect(
        database="DB_WebStudent",
        user='postgres',
        password='postgres123',
        host='localhost',
        port=5432
    )
    cursor = conn.cursor()
    script = 'SELECT * FROM "UserTypes"'
    cursor.execute(script)
    print(cursor.fetchall())

    try:
        conn = psycopg2.connect(
            database="DB_WebStudent",
            user='postgres',
            password='postgres123',
            host='localhost',
            port=5432
        )
        cursor = conn.cursor()
        script = 'SELECT * FROM "UserTypes"'
        # script = 'SELECT * FROM "DB_WebStudent".public.tables.UserTypes'
        cursor.execute(script)
        print(cursor.fetchall())

    except Exception as error:
        print("Error! Please check database configuration!")

    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()


def insert_data(data):
    # insert_script = 'INSERT INTO Users'
    pass


def fetch_all_data():
    pass


connect()

#
# def read(connection):
#     print("Read")
#
#     cursor = connection.cursor()
#     cursor.execute("select * from Dummy")
#     for row in cursor:
#         print(f'row = {row}')
#     print()
#
#
# def create(connection):
#     pass
#
#
# def update(connection):
#     pass
#
#
# def delete(connection):
#     print("Delete")
#     pass
