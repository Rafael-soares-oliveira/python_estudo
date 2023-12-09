import sys
import PySide6.QtWidgets as qtwidgets
import PySide6.QtCore as qtcore

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> CentralWidget (central_widget)
#       -> Layout (layout)
#           -> Widget 1 (botao)
#           -> Widget ...

app = qtwidgets.QApplication(sys.argv)
window = qtwidgets.QMainWindow()
window.setWindowTitle('Titulo da janela')

central_widget = qtwidgets.QWidget()
window.setCentralWidget(central_widget)

botao = qtwidgets.QPushButton('botão 1!')
botao.setStyleSheet('font-size: 10px;')

botao2 = qtwidgets.QPushButton('botão 2!')
botao2.setStyleSheet('font-size: 10px;')

botao3 = qtwidgets.QPushButton('botão 3!')
botao3.setStyleSheet('font-size: 10px;')

layout = qtwidgets.QGridLayout()  # localiza os elementos por linha/coluna
# elemento, linha, coluna, linha expande, coluna expande
layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 2, 1, 1, 2)

central_widget.setLayout(layout)


@qtcore.Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@qtcore.Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@qtcore.Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)

botao.clicked.connect(terceiro_slot(segunda_acao))

window.resize(300, 500)
window.show()
app.exec()
