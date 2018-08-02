# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 19:22:04
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 19:30:56

# Checkbutton 组件是多选按钮
# Radiobutton 是单选按钮

from tkinter import *

root = Tk()
# 需要一个Tkinter变量，用于表示该按钮是否被选择
v = IntVar()
c = Checkbutton(root, text = "测试一下", variable = v)
c.pack()
# 如果别被选中，那么变量v被赋值为1，否则为0
# 可以用个Label标签动态地展示出来
l = Label(root, textvariable = v)
l.pack()

mainloop()