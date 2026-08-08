from PyQt6.QtWidgets import (
    QWidget,QPushButton
    ,QLabel,QLineEdit,QGridLayout,
)
import sys
import os
import settings

class MasterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.front_layout = QGridLayout()
        self.setLayout(self.front_layout)
        self.button1 = QPushButton("Create Password")
        self.input1 =  QLineEdit()
        self.front_layout.addWidget(self.button1,1,1)
        self.front_layout.addWidget(self.input1,0,1)
        self.front_layout.addWidget(QLabel("Master Password"),0,0)