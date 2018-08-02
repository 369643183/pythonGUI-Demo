# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 19:33:27
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 19:39:06

from tkinter import * 

root = Tk()
v = StringVar()

def test(content, reason, name):
    if content == "1234":
        print("正确")
        print(content, reason, name)
        return True
    else:
        print("错误")
        print(content, reason, name)
        return False

testCMD = root.register(test)
e1 = Entry(root, textvariable = v, validate = "focusout", validatecommand = (testCMD, '%P', '%v', '%W'))
e2 = Entry(root)
e1.pack(padx = 20, pady = 20)
e2.pack(padx = 20, pady = 20)

mainloop()