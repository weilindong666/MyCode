# --coding:utf-8--
'''
@File: listeningUI.py
@Author:魏林栋（welindong）
@Time: 2021年10月02日  13:07
'''
from tkinter import *
from ui.mainUI import mainUI
import tkinter.font as tf


class listeningUI():
    def __init__(self):
        # mainUI.__init__(self)
        self.root = Tk()
        self.root.title("听写")
        self.root.geometry('300x200')
        # ft = tf.Font(family='楷体', size=25)
        # self.t1 = Text(self.root, width=20, height=5, font=ft)
        self.t2 = Text(self.root, width=50, height=1)
        self.listview = Listbox(self.root)
        self.scrollbar = Scrollbar(self.root)



        a = StringVar()
        self.t2.insert(END, 'I love Fishc.com')
        self.t2.tag_add('link', 1.0, 'end')
        # link = f"第{i}项"
        a.set('666')
        a.tag_add('link', '<Enter>', self.jjj)
        # list_var.set([self.t2, self.t2])

        self.listview.config(yscrollcommand=self.scrollbar.set,listvariable=a)
        self.scrollbar.config(command=self.listview.yview)
        self.listview.pack(side=LEFT, fill=Y)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.t2.pack()
        self.root.mainloop()

    def jjj(self):
        print('666')


if __name__ == '__main__':
    listeningUI()
