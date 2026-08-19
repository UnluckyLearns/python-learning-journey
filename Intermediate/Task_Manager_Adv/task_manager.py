#  /  @  > < [] {}
from database import Database
class TaskManager():
    def __init__(self):
        self.task_list = []
        self.db = Database()
        self.db.create_table()

    def fetch(self,search,completed):
        self.task_list = self.db.fetch_db(search,completed)

    def fetch_one(self,id):
        return self.db.fetch_one(id)

    def insert(self,task):
        return self.db.insert_db(task)

    def update(self,new_update,id):
        return self.db.update_one(new_update,id)

    def delete(self,id):
        return self.db.delete_one(id)
