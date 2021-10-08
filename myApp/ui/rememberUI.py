# --coding: utf - 8 - -
'''
@File: rememberUI.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
from tkinter import *

import tkinter.font as tf
from ui.mainUI import mainUI


class rememberUI(mainUI):
    def __init__(self):
        mainUI.__init__(self)
        # 基础参数
        self.point = 0
        self.noword = None
        self.nowtransform = None
        # UI
        self.root = Tk()
        self.root.title("背单词")
        self.root.geometry('520x400')
        # self.text = StringVar()
        # self.text.set("Test")
        # self.label = Label(self.root, textvariable=self.text)
        # self.label.grid(row=0, column=0)
        ft = tf.Font(family='楷体', size=25)
        self.t1 = Text(self.root, width=15, height=5, font = ft)
        self.t2 = Text(self.root, width=15, height=5, font = ft)
        self.b1 = Button(self.root, text='下一个', width=10, command=self.next)
        self.b2 = Button(self.root, text='再读一遍', width=10, command=self.again)
        self.b3 = Button(self.root, text='上一个', width=10, command=self.last)
        self.b4 = Button(self.root, text='开始', width=10, command=self.start)
        self.b4.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.mainloop()

    def start(self):
        self.b4.destroy()
        self.t1.grid(row=1, column=0)
        self.t2.grid(row=1, column=1)
        self.b1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.b2.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.b3.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.findWord()
        self.show()
        self.tool.downLoadAndRead(self.noword)
        self.exceltool.writeInfo(self.nowtime, self.noword, self.nowtransform, 0, 0)


    def next(self):
        if self.point < len(self.leftwords):
            self.point += 1
            self.findWord()
            # self.text.set(self.noword +'\n' + self.nowtransform)
            self.show()
            self.tool.downLoadAndRead(self.noword)
            self.exceltool.writeInfo(self.nowtime, self.noword, self.nowtransform, 0, 0)
        else:
            self.clean()
            self.t1.insert('end', '已经没有单词可以背了！')


    def again(self):
        self.tool.read(self.noword)


    def last(self):
        if self.point > 0:
            self.point -= 1
            self.findWord()
            self.show()
            self.tool.read(self.noword)
        else:
            self.clean()
            self.t1.insert('end', '请点“下一个”！')


    def findWord(self):
        self.noword = self.leftwords[self.point][:self.leftwords[self.point].find(',')]
        # print(word)
        self.nowtransform = self.leftwords[self.point][self.leftwords[self.point].find(',') + 1:]

    def show(self):
        self.clean()
        self.t1.insert('end', self.noword)
        self.t2.insert('end', self.nowtransform)

    def clean(self):
        self.t1.delete(0.0, 'end')
        self.t2.delete(0.0, 'end')

if __name__ == '__main__':
    rememberUI()