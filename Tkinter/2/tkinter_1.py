# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-23 19:53:04
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 10:04:02

# page:208

import Tkinter as tk
#注意：Python3.x 版本使用的库名为tkinter,小写字母t
#import tkinter as tk


#创建一个主窗口对象叫root，用于容纳整个GUI程序
#有的是写 root = Tk() 不知道为什么？可能是因为 import Tkinter as tk 而有的是import Tkinter *
root = tk.Tk()

#设置主窗口root的标题
root.title("PythoGUI")

# Label标签控件；可以显示文本和位图
# 通过Label控件在主窗口root中创建一个叫theLabel的标签部件对象，并设置text文本
theLabel = tk.Label(root,text="Python窗口程序")

# 调用pack()方法，用于自动调节部件的尺寸
# 将theLabel添加到主窗口中
theLabel.pack()

# 让主窗口工作起来
root.mainloop()
