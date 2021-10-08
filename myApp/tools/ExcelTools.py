# --coding:utf-8--
'''
@File: ExcelTools.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
import xlrd
import xlwt
import openpyxl


class ExcelTools(object):
    def __init__(self, path, time):
        self.address = path + '/record.xlsx'
        self.nowtime = time
        self.excel = openpyxl.load_workbook(self.address)
        self.sheetnames = self.excel.sheetnames
        self.addSheet()


    def writeInfo(self, sheet, word, transform, renum, wrnum):
        '''
        :param sheet: 页面名称，及日期
        :param word: 单词
        :param transform: 翻译
        :param renum: 听写次数
        :param wrnum: 错误次数
        :return:
        '''
        table = self.excel[sheet]
        nrows = table.max_row
        if table.cell(1, 1).value is None:
            self.write(table, 1, word, transform, renum, wrnum)
            self.excel.save(self.address)
            return
        self.write(table, nrows + 1, word, transform, renum, wrnum)
        self.excel.save(self.address)


    def write(self, table, row, word, transform, renum, wrnum):
        table.cell(row, 1).value = word
        table.cell(row, 2).value = transform
        table.cell(row, 3).value = renum
        table.cell(row, 4).value = wrnum


    def addSheet(self):
        if self.sheetnames[-1] != self.nowtime:
            self.excel.create_sheet(self.nowtime)
            self.excel.save(self.address)


    def readExcel(self):
        allwords = []
        recordict = {}
        for sheet in self.sheetnames:
            recordict[sheet] = {}
            table = self.excel[sheet]
            for row in range(1, table.max_row + 1):
                allwords.append(table.cell(row, 1).value + ',' + table.cell(row, 2).value)
                recordict[sheet][table.cell(row, 1).value] = [row, table.cell(row, 2).value, table.cell(row, 3).value, table.cell(row, 4).value]
        return allwords, recordict


if __name__ == '__main__':
    e = ExcelTools('C:/Users/user/Desktop/myApp/tools')
    # e.writeInfo('2021-10-02', 666, 0)
    e.readExcel()