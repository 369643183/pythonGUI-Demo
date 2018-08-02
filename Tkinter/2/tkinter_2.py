# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 11:21:17
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 19:20:10

# 报错报错报错报错报错报错报错报错报错报错报错报错报错报错报错报错报错报错

import tkinter as tk

class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        # frame.pack()
        frame.pack(side = tk.LEFT, padx = 30, pady = 60)
        self.hi_there = tk.Button(frame, text="hello python", fg = "blue", bg = "red", command = self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("进阶版本")

root = tk.Tk()
app = App(root)
root.mainloop()




# 可以通过修改 pacK() 方法的 side 参数，
# side 参数可以设置 LEF、RIGHT、TOP、TOTTOM，默认的设置时 side=tkinter.TOP


#######################################################################
# import Tkinter表示：导入Tkinter

# from Tkinter import * 表示：从Tkinter导入*（*所有东西）

# import Tkinter
# root = Tkinter.Tk()
# 或者
# from Tkinter import *
# root = Tk()

# import Tkinter 和 import Tkinter as tk 的区别是import Tkinter as tk 为Tkintere取了个别名叫tk


# import Tkinter as tk 这样的导入方法，在实例化的时候就 button2 = tk.Button()