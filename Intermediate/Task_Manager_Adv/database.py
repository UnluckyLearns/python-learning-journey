import sqlite3
from settings import * 


class Database():
    def __init__(self):
        self.command_create = """CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,task TEXT,description TEXT,completed BOOLEAN)"""
        self.command_insert = "INSERT INTO tasks(task,description,completed) VALUES (?,?,?) RETURNING id,task,description,completed"
        self.command_get = "SELECT * FROM tasks"
        self.command_get_one = "SELECT * FROM tasks WHERE id = ?"
        self.command_update = "UPDATE tasks SET task = COALESCE(?,task), description = COALESCE(?,description),completed= COALESCE(?,completed) WHERE id = ? RETURNING id,task,description,completed"
        self.command_delete_one = "DELETE FROM tasks where id = ?"
        self.command_search_completed = "SELECT *  FROM tasks WHERE (task LIKE '%' || ? || '%' OR description LIKE '%' || ? || '%') AND completed = ?"
        self.command_search = "SELECT *  FROM tasks WHERE task LIKE '%' || ? || '%' OR description LIKE '%' || ? || '%'"
        self.command_completed = "SELECT * FROM tasks WHERE completed = ?"


    def create_table(self):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
        cursor.execute(self.command_create)
        connection.commit()

    def fetch_db(self,search,completed):
        with sqlite3.connect(DB_PATH) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            if search and completed != None:
                cursor.execute(self.command_search_completed,(search,search,completed))
            elif search:
                cursor.execute(self.command_search,(search,search))
            elif completed != None:
                cursor.execute(self.command_completed,(completed,))
            else : 
                cursor.execute(self.command_get)
            d = cursor.fetchall()
            dict_list = [dict(r) for r in d]
        return dict_list

    def insert_db(self,task):
        with sqlite3.connect(DB_PATH) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(self.command_insert,(task.title,task.description,task.completed))
            dict_one = dict(cursor.fetchone())
            connection.commit()
        return dict_one

    def fetch_one(self,id):
        with sqlite3.connect(DB_PATH) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(self.command_get_one,(id,))
            dict_one  = cursor.fetchone()
            if dict_one == None:
                return None
            dict_one = dict(dict_one)

        return dict_one

    def update_one(self,new_update,id):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(self.command_update,(new_update.title,new_update.description,new_update.completed,id))
            dict_one = cursor.fetchone()
            if dict_one == None:
                return None
            connection.commit()
        return dict(dict_one)

    def delete_one(self,id):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(self.command_delete_one,(id,))
            connection.commit()
            if cursor.rowcount == 0:
                return False
        return True