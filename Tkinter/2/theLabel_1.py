# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 12:17:16
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 16:28:05


from tkinter import *

root = Tk()

textLabel = Label(root,text = "放置一张图片")

textLabel.pack(side = LEFT)

#支持gif格式的图片
photo = PhotoImage(file = "cdd.gif")

imaLabel = Label(root, image = photo)

imaLabel.pack(side = RIGHT)

mainloop()