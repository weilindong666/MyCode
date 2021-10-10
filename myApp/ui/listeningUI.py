# --coding:utf-8--
'''
@File: listeningUI.py
@Author:魏林栋（welindong）
@Time: 2021年10月02日  13:07
'''
from ui.mainUI import mainUI
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, QUrl, Qt
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
import random


class listeningUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        # 音乐播放器初始化
        self.player = QMediaPlayer()
        # UI
        self.ui = QUiLoader().load('ui/ui/listenUI.ui')
        self.ui.lineEdit.returnPressed.connect(self.correct)
        self.ui.reRead.clicked.connect(self.reRead)
        self.ui.correct.clicked.connect(self.correct)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        # 加载关闭按钮
        icon_img = QIcon("./close_2.png")
        self.ui.close_Button.setIcon(icon_img)
        self.ui.close_Button.clicked.connect(self.closeWindow)
        # 刚进入的时候确认按钮和输入框是不能用的
        self.ui.lineEdit.setEnabled(False)
        self.ui.correct.setEnabled(False)
        # 初始化
        self.nowlist = []
        self.initSort()
        self.point = 0


    def reRead(self):
        # self.point = 0时准备开始
        if self.point == 0:
            self.read()
            self.ui.reRead.setText('')
            icon_img = QIcon("./audio.png")  # 实例化一个QIcon对象
            self.ui.reRead.setIcon(icon_img)
            self.ui.reRead.setIconSize(QSize(80, 80))
            self.ui.lineEdit.setEnabled(True)
            self.ui.correct.setEnabled(True)
        else:
            self.read()


    def read(self):
        content = QMediaContent(QUrl(f'https://tts.youdao.com/fanyivoice?word={self.nowlist[self.point]}&le=eng&keyfrom=speaker-target'))
        self.player.setMedia(content)
        self.player.setVolume(50)
        self.player.play()

    def correct(self):
        # 将结果更新到excel表格里
        if self.point < len(self.nowlist):
            noword = self.getWord()
            # 背写次数加一
            self.exceltool.record(self.recordict[self.nowlist[self.point]][0], 4, self.recordict[self.nowlist[self.point]][3] + 1)
            if noword != self.nowlist[self.point].lower():
                # 错误次数加一
                self.exceltool.record(self.recordict[self.nowlist[self.point]][0], 5, self.recordict[self.nowlist[self.point]][3] + 1)
            # 继续读下一个
            self.point += 1
            if self.point >= len(self.nowlist):
                return
            self.read()
        return


    def initSort(self):
        # 最先背没有背过的单词, 再复习被错次数5次以上的
        newword = []
        for word, info in self.recordict.items():
            if info[3] == 0 or info[4] >= 5:
                newword.append(word)
        random.shuffle(newword)
        # 再背近两天的单词
        recentword = []
        for word, info in self.recordict.items():
            if self.nowtime - info[2] <= 100:
                recentword.append(word)
        random.shuffle(recentword)
        # 剩余的加到最后
        self.nowlist = newword + recentword + list(self.recordict.keys())
        self.nowlist = self.listSort(self.nowlist)


    def getWord(self):
        word = self.ui.lineEdit.text()
        self.ui.lineEdit.setText('')
        return word.strip().lower()


    def closeWindow(self):
        self.ui.close()


    def listSort(self, target):
        result = target
        pointer = 0
        while pointer < len(result) - 1:
            tword = result[pointer]
            index = pointer + 1
            while index < len(result):
                oword = result[index]
                if tword == oword:
                    result.pop(index)
                index += 1
            pointer += 1
        return result