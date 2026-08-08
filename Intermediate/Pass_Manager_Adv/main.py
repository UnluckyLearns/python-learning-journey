from UI.interface import Window
from PyQt6.QtWidgets import (
    QApplication
)
import sys
class  main():
    def __init__(self):
        self.app = QApplication([])
        self.window = Window()
        self.window.show()
        sys.exit(self.app.exec())
    


if __name__ == "__main__":
    main()