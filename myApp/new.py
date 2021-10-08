from tkinter import *
import pygame
import random

music = ["song1.mp3", "song2.mp3"]  # 注意！这里面是你下载在文件夹里的音乐文件名称。
i = 0

root = Tk()
root.title("音乐播放器")


def play():
    file = music[i]
    pygame.mixer.init()
    pygame.mixer.music.load(file)  # 加载本地文件

    pygame.mixer.music.play()  # 播放音乐

    print(i)


def stop():
    pygame.mixer.music.stop()  # 停止音乐


def suiji_song():
    global i  # 让“i”函数可以在所有def中使用
    i = random.randint(0, 1)  # 注意！这里的“4”是你的音乐文件数量减一，我有五首歌，所以是四。
    play()  # 随机播放


def next_song():  # 下一首
    stop()
    global i
    if i == 1:  # 注意！这里的“4”是你的音乐文件数量减一，我有五首歌，所以是四。
        i = 0
    else:
        i = i + 1
    play()


def last_song():  # 上一首
    stop()
    global i
    if i == 0:
        i = 1  # 注意！这里的“4”是你的音乐文件数量减一，我有五首歌，所以是四。
    else:
        i = i - 1
    play()


b1 = Button(root, text="随机开始", width=10, command=suiji_song)
b1.grid(row=0, column=0, padx=10, pady=10)

b2 = Button(root, text="下一首", width=10, command=next_song)
b2.grid(row=0, column=1, padx=10, pady=10)

b3 = Button(root, text="上一首", width=10, command=last_song)
b3.grid(row=0, column=2, padx=10, pady=10)

b4 = Button(root, text="停止", width=20, command=stop)
b4.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

b5 = Button(root, text="退出", width=20, command=root.destroy)
b5.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
root.mainloop()

