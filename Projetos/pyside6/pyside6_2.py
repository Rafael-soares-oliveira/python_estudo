import sys
import random
from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            "Hello World", alignment=QtCore.Qt.AlignCenter)  # type:ignore

        self.layout = QtWidgets.QVBoxLayout(self)  # type: ignore
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(200, 200)
    widget.show()

    sys.exit(app.exec())
