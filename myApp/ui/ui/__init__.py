# --coding:utf-8--
'''
@File: __init__.py
@Author:魏林栋（welindong）
@Time: Y E A R 年 {YEAR}年YEAR年{MONTH}月D A Y 日 {DAY}日DAY日{HOUR}
'''
# import xlrd
# import os
#
#
# def read_excel():
#     wb = xlrd.open_workbook('record.xlsx')  # 打开文件
#     print(wb.sheet_names())  # 获取所有表格名字
#     sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
#     sheet2 = wb.sheet_by_name('day_1')  # 通过名字获取表格
#     print(sheet1, sheet2)
#     print(sheet1.name, sheet1.nrows, sheet1.ncols)
#     rows = sheet1.row_values(0)  # 获取行内容
#     cols = sheet1.col_values(0)  # 获取列内容
#     print(rows)
#     print(cols)
#     # print(sheet1.cell(1, 0).value)  # 获取表格里的内容，三种方式
#     # print(sheet1.cell_value(1, 0))
#     # print(sheet1.row(1)[0].value)
# if __name__ == '__main__':
#     read_excel()
