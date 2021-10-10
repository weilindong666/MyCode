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
from ui.mainUI import mainUI
from ui.widgetUI import WidgetUI
from PySide2.QtCore import Qt


class mainPage(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        self.ui = QUiLoader().load('ui/ui/mainUI.ui')
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        # 给关闭按钮加一个图片
        icon_img = QIcon("./close_2.png")
        self.ui.close_Button.setIcon(icon_img)
        self.ui.close_Button.clicked.connect(self.closeWindow)
        self.ui.B_learn.clicked.connect(self.learnWindow)
        self.ui.B_listen.clicked.connect(self.listeningWindow)


    def learnWindow(self):
        self.ui.close()
        global ui_learn
        ui_learn.ui.show()
        ui_learn.start()


    def listeningWindow(self):
        if self.recordict:
            global ui_listen
            self.ui.close()
            ui_listen.ui.show()
        else:
            global ui_widget
            # ui_widget.start()
            ui_widget.ui.show()


    def closeWindow(self):
        self.ui.close()

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('111.png'))
    ui_main = mainPage()
    ui_main.ui.show()
    ui_learn = rememberUI()
    ui_listen = listeningUI()
    ui_widget = WidgetUI()
    app.exec_()