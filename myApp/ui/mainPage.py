# --coding:utf-8--
'''
@File: mainPage.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
from tkinter import *
from ui.rememberUI import rememberUI
from ui.listeningUI import listeningUI

class mainPage(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("背单词")
        self.root.geometry('250x100')
        self.b1 = Button(self.root, text='背单词', width=10, command=self.rememberWindow)
        self.b1.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.b2 = Button(self.root, text='听写', width=10, command=self.listeningWindow)
        self.b2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.root.mainloop()

    def rememberWindow(self):
        self.root.destroy()
        rememberUI()


    def listeningWindow(self):
        self.root.destroy()
        listeningUI()