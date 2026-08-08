from PyQt6.QtWidgets import (
    QWidget,QPushButton,QGridLayout,
    QTableWidget,QTableWidgetItem,QHeaderView
)
import sys
import os
import settings

class VaultPage(QWidget):
    def __init__(self):
        super().__init__()
        self.vault_layout = QGridLayout()
        self.setLayout(self.vault_layout)
        self.vault_table = QTableWidget()
        self.vault_table.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch)
        self.vault_buttons = {"Add" : QPushButton("Add Password"), "Delete" : QPushButton("Delete Password") ,"Search" : QPushButton("Search")}


    def create_widgets(self):
        i = 0 
        self.vault_table.setColumnCount(4)
        self.vault_table.setHorizontalHeaderLabels(["id","Website", "Username", "Password"])
        self.vault_table.setColumnHidden(0,True)
        for button in self.vault_buttons:
            self.vault_layout.addWidget(self.vault_buttons[button],7,i)
            i+=1
        self.vault_layout.addWidget(self.vault_table, 0, 0, 6, 6) 

    def fill_layout(self,db):
        self.vault_table.setRowCount(len(db.data))
        for row , data in enumerate(db.data):
            for col,value in enumerate(data):
                self.vault_table.setItem(row,col,QTableWidgetItem(str(value)))
        
        


    def get_info(self):
        if self.vault_table.selectedItems():
            if self.vault_table.currentItem().column() == 3:
                id = self.vault_table.item(self.vault_table.currentItem().row(),0).text()
                return (id,self.vault_table.currentItem().text())
            else:
                return (None,None)
        return (None,None)