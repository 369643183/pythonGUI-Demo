# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 20:37:55
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 20:53:26

"""
为某组件安装垂直滚动条，需要做两件事：
(1)设置该组件的 yscrollcommand 选项为 Scrollbar 组件的 set() 方法
(2)设置 Scrollbar 组件的 command 选项为该组件的 yview() 方法
"""

from tkinter import *

root = Tk()
sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)
lb = Listbox(root, yscrollcommand = sb.set)
for i in range(50):
    lb.insert(END, str(i))
lb.pack(side = LEFT, fill = BOTH)
sb.config(command = lb.yview)

mainloop()

"""
其实，这是个互联互通的过程。
当用户操作滚动条进行滚动的时候，滚动条响应滚动那并同时通过 Listbox 组件的 yview() 方法滚动列表框里的内容；
同样，当列表框中可视范围发生变化的时候，Listbox 组件通过调用 Scrollbar 组件的 set() 方法设置滚动条的最新位置。
"""