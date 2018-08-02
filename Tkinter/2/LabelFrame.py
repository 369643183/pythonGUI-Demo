# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 19:57:07
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 20:15:40

# LabelFrame 组件是 Frame 框架的进化版，就是添加了 Label 的 Frame，
# 能使得 Checkbutton 和 Radiobutton 的组件变得更简单

from tkinter import *

root = Tk()
root.title("标题还是要有的")
group = LabelFrame(root, text = "最好的脚本语言是？", padx = 10, pady = 10)
group.pack(padx = 10, pady = 20)
LANGUAGE = [('python', 1),
            ('php', 2),
            ('javascript', 3),
            ('perl', 4)]
v = IntVar()
v.set(1)
for lang, num in LANGUAGE:
    b = Radiobutton(group, text = lang, variable = v, value = num)
    b.pack(anchor = W)

mainloop()
