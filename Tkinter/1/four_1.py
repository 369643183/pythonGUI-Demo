# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 10:38:44
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 10:43:24

# 使用网格管理器很容易，只需要告诉小部件在网格管理器中的第几行第几列，也不用预先指定网格管理器的大小，它会根据内部的小部件来设定自己的大小。

from Tkinter import *

master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()