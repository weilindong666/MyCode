# -*- coding:utf-8 -*-
"""
    @Time : 2021/9/24 14:01
    @Author: Wei Lindong
    @File: main.py
    @Software: PyCharm
"""
from tools.ReferTools import ReferTools
import os
from tools.ExcelTools import ExcelTools
import time


class mainUI(object):
    def __init__(self):
        self.allwords = []
        self.record = []
        self.leftwordss = []
        self.num = 0
        self.mainpath = os.getcwd()
        self.tool = ReferTools()
        self.nowtime = time.strftime("%Y-%m-%d", time.localtime())
        self.exceltool = ExcelTools(self.mainpath, self.nowtime)
        self.recordict = {}
        self.readRecord()


    def readRecord(self):
        with open(self.mainpath + '/SGSC4.csv', 'r', encoding='utf-8') as f:
            self.allwords = f.readlines()
        self.record, self.recordict = self.exceltool.readExcel()
        self.leftwords = list(set(self.allwords) - set(self.record))
        self.num = len(self.leftwords)


if __name__ == '__main__':
    mainPage = mainUI()
    print(mainPage.allwords)