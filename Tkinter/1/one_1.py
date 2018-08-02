#!/usr/bin/python
# -*- coding: UTF-8 -*-
#不写上面这行coding：utf-8 的话则代码中不能出现中文，否则会报错

#最简单的GUI窗口，标题是默认的tk，无内容


from Tkinter import *

#创建主窗口
root = Tk()
#root= Tk(className='标题')#创建主窗口并设置标题

#mainloop是主窗口的成员函数，也就是表示让这个root工作起来，开始接收鼠标的和键盘的操作。通过鼠标缩放以及关闭这个窗口。
root.mainloop()


# Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。