from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Редактор текста")
        self.setGeometry(250, 200, 650, 750)

        self.text_edit = QtWidgets.QTextEdit(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(55)
        self.text_edit.setFont(font)

        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)

        self.fileMenu = QMenu("Файл", self)
        self.fileMenu.addAction("Открыть", self.action_clicked)
        self.fileMenu.addAction("Сохранить", self.action_clicked)

        self.menuBar.addMenu(self.fileMenu)

        self.setMenuBar(self.menuBar)

    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                with open(fname, 'r') as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
               print("erron_open")
        else:
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                with open(fname, 'w') as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("erron_save")


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
