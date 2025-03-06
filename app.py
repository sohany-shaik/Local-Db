import sqlite3
import datetime
# create database
def create_db():
    conn = sqlite3.connect("test.db")
    if conn:
        print("Database created")
        return conn
    else:
        print("Db creation failed")
        return None

# TABLE CREATION
# Task name, description, created date
def create_table():
    try:
        conn = create_db()
        query = """
        # create table tablename
        CREATE TABLE todos_table
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            created_date datetime NOT NULL
            )
        """
        cursor = conn.execute(query)
        if cursor:
            print("Table created")
    except Exception as e:
        print(f"Exception occured while creating table {e}")
    finally:
        conn.close()
def insert_data(task_name,description,created_date):
    conn = create_db()
    query = """
    INSERT INTO todos_table(name,description,created_date)
    VALUES(?,?,?)
    """
    conn.execute(query,[task_name,description,created_date])
    conn.commit()
    conn.close()

def get_all_data():
    conn = create_db()
    query = """
    SELECT * FROM todos_table
    """
    result = conn.execute(query)
    for row in result:
        print(row)

def query_data(id,name):
    conn = create_db()
    query = """
    SELECT * FROM todos_table WHERE ID=? OR name = ?
    """
    result = conn.execute(query,[id,name])
    for row in result:
        print(row)


def update_data(description,id):
    conn = create_db()
    query = """
        UPDATE todos_table set description = ? WHERE id=?
    """   
    conn.execute(query,[description,id])
    conn.commit()
    conn.close()

def delete_data(id):
    conn = create_db()
    query = """
        DELETE FROM todos_table WHERE ID=?;
    """   
    conn.execute(query,[id])
    conn.commit()
    conn.close()
now = datetime.datetime.now()

# insert_data("Task 10","Description 10",now)
# update_data("New updated desc of task 3",3)
# delete_data(2)
# query_data()
get_all_data()

# query_data(5,"Task 4")
  

