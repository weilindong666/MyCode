# --coding: utf - 8 - -
'''
@File: rememberUI.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
from PySide2.QtUiTools import QUiLoader
from ui.mainUI import mainUI
from threading import Thread
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl, Qt
from PySide2.QtGui import QIcon


class rememberUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        # 基础参数
        self.point = 0
        self.noword = None
        self.nowtransform = None
        # UI
        self.player = QMediaPlayer()
        self.ui = QUiLoader().load('ui/ui/learnUI.ui')
        # 隐藏顶部边框
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        # 添加关闭按钮
        icon_img = QIcon("./close_2.png")
        self.ui.close_Button.setIcon(icon_img)
        self.ui.close_Button.clicked.connect(self.closeWindow)

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
            self.point -= 1


    def findWord(self):
        self.noword = self.leftwords[self.point][:self.leftwords[self.point].find(',')]
        self.nowtransform = self.leftwords[self.point][self.leftwords[self.point].find(',') + 1:]

    def show(self):
        self.ui.WORD.setText(self.noword)
        self.ui.TRANS.setText(self.nowtransform)


    def downLoadAndRead(self):
        content = QMediaContent(QUrl(f'https://tts.youdao.com/fanyivoice?word={self.noword}&le=eng&keyfrom=speaker-target'))
        self.player.setMedia(content)
        self.player.setVolume(50)
        self.player.play()
        # self.tool.downLoadAndRead(self.noword)

    def read(self):
        content = QMediaContent(QUrl(f'https://tts.youdao.com/fanyivoice?word={self.noword}&le=eng&keyfrom=speaker-target'))
        self.player.setMedia(content)
        self.player.setVolume(50)
        self.player.play()
        # self.tool.read(self.noword)

    def closeWindow(self):
        self.ui.close()