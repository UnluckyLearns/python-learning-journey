from PyQt6.QtWidgets import (
    QWidget,QVBoxLayout,QStackedWidget
)
import os
import sys
import database
import encryption
import settings
from .front_page import FrontPage
from .vault_page import VaultPage
from .master_page import MasterPage
from .popup import AddDialog, DelDialog, SearchDialog
from database import Database

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.db.create_db()
        self.setWindowTitle("Pass Manager")
        self.main_layout = QVBoxLayout(self)
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        self.page_front = FrontPage()
        self.page_vault = VaultPage()
        self.page_master = MasterPage()


        self.add_dialog = AddDialog()
        self.del_dialog = DelDialog()
        self.search_dialog = SearchDialog()


        self.db.fetch_master()
        self.stacked_widget.addWidget(self.page_front)
        self.stacked_widget.addWidget(self.page_master)
        self.stacked_widget.addWidget(self.page_vault)
        if not self.db.data_master:
            self.stacked_widget.setCurrentIndex(1)
        self.page_vault.create_widgets()


        self.page_master.button1.clicked.connect(lambda : self.db.insert_master(self.page_master.input1.text(),self.stacked_widget))
        self.page_front.button1.clicked.connect(self.change_page)
        self.page_vault.vault_buttons["Add"].clicked.connect(self.add_pop_up)
        self.page_vault.vault_buttons["Delete"].clicked.connect(self.delete_pop_up)
        self.page_vault.vault_buttons["Edit"].clicked.connect(self.edit_pass)
        self.page_vault.vault_buttons["Search"].clicked.connect(self.search_pop_up)

        self.del_dialog.button_del.clicked.connect(self.delete_insert)
        self.add_dialog.button.clicked.connect(self.add_insert)
        self.search_dialog.input_website.textChanged.connect(self.search_web)

    def change_page(self):
        i = 0
        self.db.fetch_master()
        if self.db.data_master:
            self.stacked_widget.setCurrentIndex(0)
            if encryption.check_pass(self.page_front.input1.text(),self.db.data_master[0]):
                self.db.fetch_db()
                self.page_vault.fill_layout(self.db)
                self.stacked_widget.setCurrentIndex(2)
            else:
                self.page_front.label.setVisible(True)
            

    def add_pop_up(self):
        self.add_dialog.show()

    def search_pop_up(self):
        self.search_dialog.show()

    def delete_pop_up(self):
        self.del_dialog.show()

    def edit_pass(self):
        id,new_pass = self.page_vault.get_info()
        if new_pass:
            new_pass = encryption.hash_pass(new_pass)
            self.db.edit_pass_db(new_pass,id)
            self.db.fetch_db()
            self.page_vault.fill_layout(self.db)

    def add_insert(self):
        website = self.add_dialog.input_website.text()
        username = self.add_dialog.input_user.text()
        password = encryption.hash_pass(self.add_dialog.input_password.text())
        self.db.insert_db(website,username,password)
        self.db.fetch_db()
        self.page_vault.fill_layout(self.db)

    def  delete_insert(self):
        website = self.del_dialog.input_website.text()
        self.db.delete_db(website)
        self.db.fetch_db()
        self.page_vault.fill_layout(self.db)


    def search_web(self):
        self.db.search_web_db(self.search_dialog.input_website.text())
        self.page_vault.fill_layout(self.db)
    