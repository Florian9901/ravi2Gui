import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Fichier")
        self.initUI()

        # Exit QAction
        open_action = QAction("Ouvrir", self)
        save_action = QAction("Enregistrer", self)
        exit_action = QAction("Quitter", self)
        open_action.setStatusTip('Ouvrir un ficher')
        save_action.setStatusTip('Sauvegarder le fichier')
        exit_action.setStatusTip('Quitter la fenêtre')
        self.file_menu.addAction(open_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(exit_action)



    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Jeux')
        self.resize(1280, 720)
        self.show()


