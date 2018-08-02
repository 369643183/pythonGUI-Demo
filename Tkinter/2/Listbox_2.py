# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 20:26:01
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 20:36:59

from tkinter import *

root = Tk()
# 创建空列表
theLb = Listbox(root, setgrid = True)
# Listbox 默认只显示 10 个项目，解决办法是设置 height 的值
# theLb = Listbox(root, setgrid = True, height = 11)
theLb.pack()
# 往里面添加数据
for item in range(11):
    theLb.insert(END, item)

mainloop()