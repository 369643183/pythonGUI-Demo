# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 16:29:36
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 16:38:06

from tkinter import *

root = Tk()
photo = PhotoImage(file = "cdd.gif") #需要使用gif格式的图片
theLabel = Label(root, 
    text = "好好学习\n天天向上",
    justify = LEFT,
    image = photo,
    compound = CENTER,
    font = ("微软雅黑", 20),
    fg = "red"
    )
theLabel.pack()

mainloop()