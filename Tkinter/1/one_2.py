#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk(className='标题')
label = Label(root)
label['text'] = '内容呀'
label.pack()
root.mainloop()