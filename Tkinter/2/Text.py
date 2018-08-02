# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 21:11:50
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 21:15:13

from tkinter import *

root = Tk()
text = Text(root, width = 30, height = 10)
text.pack()
# INSERT索引表示插入光标当前位置
text.insert(INSERT, "人生苦短\n")
text.insert(END, "我用python")

mainloop()