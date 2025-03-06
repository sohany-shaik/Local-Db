import sqlite3
import datetime
# create database

class LocalDb:
    def __init__(self,db_name,table_name):
        self.db_name = db_name
        self.table_name = table_name
        if not self.table_exists():
            self.create_table()
        
    def create_conn(self):
        conn = sqlite3.connect(self.db_name)
        if conn:
            print("Database created")
            return conn
        else:
            print("Db creation failed")
            return None

    def create_table(self):
        conn = self.create_conn()
        try:
            query = f"""
             
            CREATE TABLE {self.table_name}
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
  
    def insert_data(self,task_name,description,created_date):
        conn = self.create_conn()
        query = f"""
        INSERT INTO {self.table_name}(name,description,created_date)
        VALUES(?,?,?)
        """
        conn.execute(query,[task_name,description,created_date])
        conn.commit()
        conn.close()

    def get_all_data(self):
        conn = self.create_conn()
        query = f"""
        SELECT * FROM {self.table_name}
        """
        result = conn.execute(query)
        data_list = []
        for row in result:
            print(row)
            row_dict = {
                "task" : row[1], 
                "description" : row[2], 
                "created_at" : row[3], 
            }
            data_list.append(row_dict)
        return data_list
  
    def query_data(self,id,name):
        conn = create_conn()
        query = f"""
        SELECT * FROM {self.table_name} WHERE ID=? OR name = ?
        """
        result = conn.execute(query,[id,name])
        for row in result:
            print(row)

    def update_data(self,old_task,new_task,description,updated_at=datetime.datetime.now()):
        conn = self.create_conn()
        query = f"""
            UPDATE {self.table_name} set description = ?,name=?,created_date=? WHERE name=?
        """   
        conn.execute(query,[description,new_task,updated_at,old_task])
        conn.commit()
        conn.close()

    def delete_data(self,task_name):
        conn = self.create_conn()
        query = f"""
            DELETE FROM {self.table_name} WHERE name=?;
        """   
        conn.execute(query,[task_name])
        conn.commit()
        conn.close()

    def table_exists(self):
        conn = self.create_conn()
        listOfTables = conn.execute(
        f"""SELECT name FROM sqlite_master WHERE type='table' 
        AND name='{self.table_name}'; """).fetchall()
        conn.commit()
        conn.close()
        print(listOfTables)
        if listOfTables == []:
            print('Table not found!')
            return False
        else:
            print('Table found!')
            return True
        
        
