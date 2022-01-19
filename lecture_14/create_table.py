import sqlite3
from sqlite3 import Error


# This function accepts a path for the database on the computer.
# If the database doesn't exist - it creates the file automatically.
def create_connection(db_file_path):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        # This function opens a connection object with this path.
        # If there is no database in that path, it creates a file.
        conn = sqlite3.connect(db_file_path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        # This is an object of type Cursor, that i can use to make changes to my
        # database.
        cursor = conn.cursor()
        cursor.execute("""Create table projects(
            id integer Primary key,
            name text,
            begin_date text,
            end_date text);
        """)
    except Error as e:
        print(e)


if __name__ == '__main__':
    # The path I want to create my database in.
    db_path = r"./my_db.db"
    conn = create_connection(db_path)
    create_table(conn)
