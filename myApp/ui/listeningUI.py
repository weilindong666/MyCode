# --coding:utf-8--
'''
@File: listeningUI.py
@Author:魏林栋（welindong）
@Time: 2021年10月02日  13:07
'''
from ui.mainUI import mainUI
from PySide2.QtUiTools import QUiLoader
from threading import Thread


class listeningUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        self.ui = QUiLoader().load('ui/ui/listenUI.ui')


    def jjj(self):
        print('666')
