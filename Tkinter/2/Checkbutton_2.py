# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 19:31:43
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 20:12:06

from tkinter import *

root = Tk()
LANGUAGE = ['python', 'java', 'php', 'asp']
v = []
for lang in LANGUAGE:
    v.append(IntVar())
    b = Checkbutton(root, text = lang, variable = v[-1])
    b.pack(anchor = W)

mainloop()

# 可以把 Checkbutton 组件都向左边对齐
# 通过 pack() 的 anchor 选项实现，同有九个值：
# E S W N  NE  SE SW NW CENTER ，东南西北。。。自己领悟