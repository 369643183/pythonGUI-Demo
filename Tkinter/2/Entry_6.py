# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 19:40:41
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 19:55:53

"""
计算器
"""

from tkinter import *

root = Tk()
root.title("计算器")
frame = Frame(root)
frame.pack(padx = 20, pady = 20)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    # 注意，这里不能用 e1.get() 或者 v1.get() 来获取是输入的内容
    # 因为 validate 选项指定为"key"的时候，有任何输入操作都被拦截到这个函数中
    # 所以要使用 %P 来获取新的输入框内容
    if content.isdigit():
        return True
    else:
        return False

testCMD = root.register(test)

Entry(frame, textvariable = v1, width = 20, validate = "key",\
    validatecommand = (testCMD, '%P')).grid(row = 0, column = 0)

Label(frame, text = "+").grid(row = 0, column = 1)

Entry(frame, textvariable = v2, width = 20, validate = "key",\
    validatecommand = (testCMD, '%P')).grid(row = 0, column = 2)

Label(frame, text = "=").grid(row = 0, column = 3)

Entry(frame, textvariable = v3, width = 20, validate = "key",\
    validatecommand = (testCMD, '%P')).grid(row = 0, column = 4)

def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(result)

Button(frame, text = "计算结果", command = calc).grid(row = 1, column = 2, pady = 10)

mainloop()