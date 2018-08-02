# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 20:16:12
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 20:22:51

# Entry 就是输入框
# 获取输入框里面的内容可以使用 Entry 组件里的 get() 方法
# 也可以使用 tkinter 的变量（通常是 StringVar）挂钩到 textvariable 选项，
# 然后通过变量的 get() 方法获取


from tkinter import *

root = Tk()
e = Entry(root)
e.pack(padx = 20, pady = 20)
e.delete(0, END)
e.insert(0, "默认文本。。。")

mainloop()