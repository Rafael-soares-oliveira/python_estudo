import re
import sys
from PySide6.QtCore import Slot
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QApplication, QLineEdit, QLabel,
    QPushButton, QGridLayout)
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE, TEXT_MARGIN, setupTheme, MEDIUM_FONT_SIZE


#  Main window
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def addWidgetToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)


# Display
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size:{SMALL_FONT_SIZE}px;font-weight: bold;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])


# Result
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;font-weight: bold')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


# Buttons
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)


# Buttons Grid
class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['3', '2', '1', '+'],
            ['+/-', '0', '.', '=']
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialValue = 'Resultado'
        self._signal = ''
        self._left = None
        self._right = None
        self._op = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                self.addWidget(button, rowNumber, colNumber)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == '+/-':
            self._signal = '-'

        if text in '+-/*':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text in '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @ Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _negativeClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display
        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            print('Não tem nada para colocar no valor da esquerda')
            return
        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._signal} {self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print('Sem nada para a direita')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0.0

        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            print('Zero Division Error')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None


NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0


app = QApplication(sys.argv)
window = MainWindow()
display = Display()
info = Info('')

# Grid
buttonsGrid = ButtonsGrid(display, info)


if __name__ == '__main__':
    setupTheme()
    window.addWidgetToLayout(info)
    window.addWidgetToLayout(display)
    window.vLayout.addLayout(buttonsGrid)

    window.show()
    app.exec()
