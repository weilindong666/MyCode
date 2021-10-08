import os
import csv

def csvW():
    f=open('./SGSC4.csv', 'w', encoding='utf-8', newline='')
    csvw=csv.writer(f)
    return csvw



def read():
    csvw=csvW()
    path='C:/Users/Administrator/Desktop/myApp/siji.txt'
    with open(path, 'r')as f:
        info = f.readlines()
        info1 = f.readline()
        # print(info)
        # print(info1)
    for i in range(0, len(info), 2):
        csvw.writerow([info[i].replace('\n', ''), info[i+1].replace('\n', '')])
        print(info[i].replace('\n', ''), info[i+1].replace('\n', ''))

if __name__ == '__main__':
    read()













