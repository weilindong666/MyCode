# import os
# from playsound import playsound
#
# # cmd_command = f"ffmpeg -i C:/Users/user/Desktop/myApp/tools/temp.m4a -acodec pcm_s16le -ac 1 -ar 16000 -y C:/Users/user/Desktop/myApp/tools/temp.wav"
# # os.system(cmd_command)
#
#
# playsound('temp.wav')
# import openpyxl
#
# data = openpyxl.load_workbook('C:/Users/user/Desktop/myApp/ui/record.xlsx')
# data.create_sheet('1_10_2021')
# sheetnames = data.sheetnames
# print(sheetnames)
# table = data[(sheetnames[-1])]
# # table.active()
# print(table.title)
# nrows = table.max_row  # 获得行数
# ncolumns = table.max_column  # 获得列数
# print(nrows, ncolumns)
# values = ['E', 'X', 'C', 'E', 'L']
# for value in values:
#     table.cell(nrows + 1, 1).value = value
#     nrows = nrows + 1
#
# data.save('C:/Users/user/Desktop/myApp/ui/record.xlsx')