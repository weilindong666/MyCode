# --coding: utf - 8 - -
'''
@File: rememberUI.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
from PySide2.QtUiTools import QUiLoader
from ui.mainUI import mainUI
from threading import Thread


class rememberUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        # 基础参数
        self.point = 0
        self.noword = None
        self.nowtransform = None
        # UI
        self.ui = QUiLoader().load('ui/ui/learnUI.ui')
        self.ui.pushButton_2.clicked.connect(self.nextOne)
        self.ui.pushButton_1.clicked.connect(self.lastOne)
        self.ui.WORD.clicked.connect(self.again)


    def start(self):
        self.findWord()
        self.show()
        thread = Thread(target=self.downLoadAndRead)
        thread.start()
        self.exceltool.writeInfo(self.nowtime, self.noword, self.nowtransform, 0, 0)


    def nextOne(self):
        if self.point < len(self.leftwords):
            self.point += 1
            self.findWord()
            self.show()
            thread = Thread(target=self.downLoadAndRead)
            thread.start()
            self.exceltool.writeInfo(self.nowtime, self.noword, self.nowtransform, 0, 0)
        else:
            self.ui.WORD.setText('已经没有单词可以背了！！')
            self.ui.TRANS.setText('')


    def again(self):
        thread = Thread(target=self.read)
        thread.start()


    def lastOne(self):
        if self.point > 0:
            self.point -= 1
            self.findWord()
            self.show()
            thread = Thread(target=self.read)
            thread.start()
        else:
            self.ui.WORD.setText('请点下一个！！')
            self.ui.TRANS.setText('')


    def findWord(self):
        self.noword = self.leftwords[self.point][:self.leftwords[self.point].find(',')]
        self.nowtransform = self.leftwords[self.point][self.leftwords[self.point].find(',') + 1:]

    def show(self):
        self.ui.WORD.setText(self.noword)
        self.ui.TRANS.setText(self.nowtransform)


    def downLoadAndRead(self):
        self.tool.downLoadAndRead(self.noword)

    def read(self):
        self.tool.read(self.noword)