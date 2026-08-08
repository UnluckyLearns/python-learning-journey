from PyQt6.QtWidgets import (
    QPushButton,QLabel,QLineEdit,QDialog,
    QFormLayout
)
import sys
import os
import settings

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()

        self.label_user = QLabel("Username : ")
        self.label_website = QLabel("Website : ")
        self.label_password = QLabel("Password : ")

        self.input_user = QLineEdit()
        self.input_website = QLineEdit()
        self.input_password = QLineEdit()

        self.button = QPushButton("Add")


        self.layout.addRow(self.label_user, self.input_user)
        self.layout.addRow(self.label_website, self.input_website)
        self.layout.addRow(self.label_password, self.input_password)
        self.layout.addRow(self.button)
        self.setLayout(self.layout)




class DelDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.input_website = QLineEdit()
        self.label_website = QLabel("Website : ")
        self.button_del = QPushButton("Delete")
        self.layout.addRow(self.label_website, self.input_website)
        self.layout.addRow(self.button_del)
        self.setLayout(self.layout)



class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.input_website = QLineEdit()
        self.label_website = QLabel("Website : ")
        self.layout.addRow(self.label_website, self.input_website)
        self.setLayout(self.layout)


