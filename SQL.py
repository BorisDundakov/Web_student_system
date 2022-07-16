import pyodbc


def read(connection):
    print("Read")
    cursor = connection.cursor()
    cursor.execute("select * from Dummy")
    for row in cursor:
        print(f'row = {row}')
    print()


def create(connection):
    print("Create")
    cursor = connection.cursor()
    cursor.execute("insert into Dummy (a,b) values (?,?);",
                   3232, 'catzzz')

    connection.commit()
    read(connection)


def update(connection):
    print("Update")
    cursor = connection.cursor()
    cursor.execute("update Dummy set b = ? where a = ?;",
                   'dogzzz', 3232)

    connection.commit()
    read(connection)


def delete(connection):
    print("Delete")
    cursor = connection.cursor()
    cursor.execute("delete from Dummy where a > 5")
    connection.commit()
    read(connection)


connection = pyodbc.connect(
    "Driver ={ODBC Driver 11 for SQL Server};"
    "Server=HOME;"
    "Database=WebStudent DB;"
    "Trusted_Connection = yes;)"
)

create(connection)
update(connection)
delete(connection)

connection.close()
