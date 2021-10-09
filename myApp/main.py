# --coding:utf-8--
'''
@File: main.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from ui.rememberUI import rememberUI
from ui.listeningUI import listeningUI


class mainPage(object):
    def __init__(self):
        self.ui = QUiLoader().load('ui/ui/mainUI.ui')
        self.ui.B_learn.clicked.connect(self.learnWindow)
        self.ui.B_listen.clicked.connect(self.listeningWindow)
        self.ui.B_review.clicked.connect(self.reviewWindow)


    def learnWindow(self):
        self.ui.close()
        global ui_learn
        ui_learn.ui.show()
        ui_learn.start()


    def listeningWindow(self):
        self.ui.close()
        global ui_listen
        ui_listen.ui.show()


    def reviewWindow(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('111.png'))
    ui_main = mainPage()
    ui_main.ui.show()
    ui_learn = rememberUI()
    ui_listen = listeningUI()
    app.exec_()