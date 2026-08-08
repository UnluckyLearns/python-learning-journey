import sqlite3
from settings import *
import encryption
class Database():
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

        self.command_create ="""CREATE TABLE IF NOT EXISTS info(id INTEGER PRIMARY KEY, website TEXT, username TEXT, password TEXT HIDDEN)"""
        self.command_create2 ="""CREATE TABLE IF NOT EXISTS master(password TEXT)"""
        self.command_insert = "INSERT INTO info (website,username,password) VALUES (?, ?, ?) "
        self.command_delete = "DELETE FROM info WHERE website= ? "
        self.command_fetch = """SELECT id,website,username,password FROM info"""
        self.command_fetch_master = """SELECT password FROM master"""
        self.command_insert_master = "INSERT INTO master (password) VALUES (?) "
        self.command_edit_pass = "UPDATE info SET password = ? WHERE id = ?"
        self.command_search_web = "SELECT * FROM info WHERE website LIKE '%' || ? || '%'"

        self.data_master = []
        self.data = []



    def create_db(self):
        self.cursor.execute(self.command_create)
        self.cursor.execute(self.command_create2)



    def insert_master(self,passw,stacked):
        password = encryption.hash_pass(passw)
        self.cursor.execute(self.command_insert_master,(password,))
        stacked.setCurrentIndex(0)
        self.connection.commit()
    
    def insert_db(self,website,username,passwrd):
        self.cursor.execute(self.command_insert,(website,username,passwrd))
        self.connection.commit()
        self.fetch_db()
        

    def delete_db(self,select):
        self.cursor.execute(self.command_delete,(select,))
        self.connection.commit()
        self.fetch_db()

    def edit_pass_db(self,newpass,id):
        self.cursor.execute(self.command_edit_pass,(newpass,id))
        self.connection.commit()
        self.fetch_db()

    def search_web_db(self,web):
        self.cursor.execute(self.command_search_web,(web,))
        self.data = self.cursor.fetchall()

    def fetch_db(self):
        self.cursor.execute(self.command_fetch)
        self.data = self.cursor.fetchall()


    def fetch_master(self):
        self.cursor.execute(self.command_fetch_master)
        self.data_master = self.cursor.fetchone()
