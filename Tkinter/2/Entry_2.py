# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 20:23:50
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 20:42:24

from tkinter import *

root = Tk()
# Tkinter 提供了三种布局方法：pack()、 fird() 和 place()
# grid() 方法是用表格的形式类管理组件的位置
# row 选项代表行
# column 选项代表列
Label(root, text = "学校：").grid(row=0)
Label(root, text = "班级：").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row = 0, column = 1, padx = 20, pady = 10)
e2.grid(row = 1, column = 1, padx = 20, pady = 10)

def show():
    print("学校是：%s" % e1.get())
    print("班级是：%s" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

# 如果表格大于组件，那么可以使用 sticky 选项来说设置组件的位置、
# 同样需要使用 E W S N 以及 NE  SE SW NW 来表示方位

Button(root, text = "获取信息", width = 10, command = show)\
        .grid(row = 3, column = 0, sticky = W, padx = 20, pady = 10)

Button(root, text = "退出", width = 10, command = root.quit)\
        .grid(row = 3, column = 1, sticky = E, padx = 20, pady = 10)

mainloop()