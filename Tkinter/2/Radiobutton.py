# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 19:42:39
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 19:55:54

# Checkbutton 组件是多选按钮
# Radiobutton 是单选按钮

# 单选效果，让组内的 Radiobutton 同享一个 variable 选项，并且设置不同的 value 选项值

# from tkinter import *

# root = Tk()
# v = IntVar()
# Radiobutton(root, text = "One", variable = v, value = 1).pack(anchor = W)
# Radiobutton(root, text = "Two", variable = v, value = 2).pack(anchor = W)
# Radiobutton(root, text = "Three", variable = v, value = 3).pack(anchor = W)

# mainloop()


######################################
# 可以用循环来处理是代码更加简洁

from tkinter import *

root = Tk()
LANGUAGE = [
    ('python', 1),
    ('php', 2),
    ('java', 3),
    ('ruby', 4)]

v = IntVar()
v.set(1)
for lang, num in LANGUAGE:
    b = Radiobutton(root, text = lang, variable = v, value = num)
    # b = Radiobutton(root, text = lang, variable = v, value = num, indicatoron = False) #去掉前面的小圆圈
    b.pack(anchor = W)
    # b.pack(fill = X)

mainloop()