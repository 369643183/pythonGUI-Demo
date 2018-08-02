# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 20:54:16
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 21:09:39

from tkinter import *

# root = Tk()
# # 因为from本身是python 的关键字，所以后面加个_
# Scale(root, from_ = 0, to = 50).pack()
# Scale(root, from_ = 0, to = 200, orient = HORIZONTAL).pack()

# mainloop()


######## 通过 get() 方法获得当前滑块的位置
root = Tk()
s1 = Scale(root, from_ = 0, to = 50)
s1.pack()
s2 = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
s2.pack()

def show():
    print(s1.get(), s2.get())

Button(root, text = "获得位置", command = show).pack()

mainloop()