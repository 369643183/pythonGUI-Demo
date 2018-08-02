# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 10:38:44
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 11:57:08

# http://www.jianshu.com/p/5c7a1af4aa53

from Tkinter import *

master = Tk()


# grid设置部件的网格坐标，以左上角为原点向右向下延伸
# row行，cloumn列，不写的话默认值为0（或 同 行/列 部件的 右/下 边）
Label(master, text="First").grid(row=0, sticky = W)
Label(master, text="Second").grid(row=1, sticky = W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button = Button(master,text = "按钮")

# 设置让一个部件占用多个行或列。columnspan指定列数，rowspan指定行数。
# padx ,pady 使用位置管理器直接指定小部件在窗口中的x和y值来设置位置，但是它不能兼容所有的计算机，在不同分辨率的窗口上排列的位置可能会不同，所以我们尽量避免使用它
button.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5,
            pady = 5, sticky = W + E + N + S)

mainloop()


# 注意每个小部件都呆在他们自己元件的中间，你可以使用sticky选项来修改这个设置，它有四个值如下：
# 值   含义
# E   东（右）
# S   南（下）
# W   西（左）
# N   北（上）