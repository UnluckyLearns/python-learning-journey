from PyQt6.QtWidgets import (
    QWidget,QPushButton
    ,QLabel,QLineEdit,QGridLayout
)

class FrontPage(QWidget):
    def __init__(self):
        super().__init__()
        self.front_layout = QGridLayout()
        self.setLayout(self.front_layout)
        self.button1 = QPushButton("Check Password")
        self.input1 =  QLineEdit()
        self.label = QLabel("Wrong PassWord")
        self.label.setVisible(False)
        self.front_layout.addWidget(self.button1,1,1)
        self.front_layout.addWidget(self.input1,0,1)
        self.front_layout.addWidget(QLabel("Master Password"),0,0)
        self.front_layout.addWidget(self.label,2,1)
       