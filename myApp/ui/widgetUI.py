# -*- coding: UTF-8 -*-
'''
@Time    : 2021/10/10 17:52
@Author  : 魏林栋
@Site    : 
@File    : widgetUI.py
@Software: PyCharm
'''
from ui.mainUI import mainUI
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt


class WidgetUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        self.ui = QUiLoader().load('ui/ui/widget.ui')
        icon_img = QIcon("./close_2.png")  # 实例化一个QIcon对象
        self.ui.pushButton.setIcon(icon_img)
        # self.ui.pushButton.setIconSize(QSize(80, 80))
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.pushButton.clicked.connect(self.close)


    def close(self):
        self.ui.close()