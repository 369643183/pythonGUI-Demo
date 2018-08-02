# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 16:39:37
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 16:57:24

# Button组件有个command选项，用于指定一个函数或方法，当用户单击按钮的时候，tkinter就会去执行哪个函数或方法
# 添加一个按钮，当用户单击按钮后Label文本发生改变。
# 要想文本发生改变，只需要设置 textvariable 选项为 tkinter 变量即可。


from tkinter import *

def callback():
    var.set("哈哈哈哈")

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

# 创建一个文本Label对象
var = StringVar()
var.set("人生苦短，\n我用python")
textLabel = Label(frame1,
    textvariable = var,
    justify = LEFT)
textLabel.pack(side = LEFT)

# 创建一个图像Label对象
# 用 PhotoImage实例化一个图片对象（支持gif格式的图片）
photo = PhotoImage(file="bbb.gif")
imgLabel = Label(frame1, image = photo)
imgLabel.pack(side = RIGHT)

# 加个按钮
theButon = Button(frame2, text = "我不服", command = callback)
theButon.pack()
frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)

mainloop()