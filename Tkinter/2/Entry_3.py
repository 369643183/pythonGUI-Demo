# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 20:50:30
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-07 21:06:57

from tkinter import *

root = Tk()

Label(root, text = "用户名：").grid(row=0)
Label(root, text = "密码：").grid(row=1)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2, show="*")
e1.grid(row = 0, column = 1, padx = 20, pady = 10)
e2.grid(row = 1, column = 1, padx = 20, pady = 10)

def show():
    print("用户名是：%s" % v1.get())
    print("密码是：%s" % v2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text = "登录", width = 10, command = show)\
        .grid(row = 3, column = 0, sticky = W, padx = 20, pady = 10)

Button(root, text = "取消", width = 10, command = root.quit)\
        .grid(row = 3, column = 1, sticky = E, padx = 20, pady = 10)

mainloop()

"""
Entry 组件支持验证输入内容的合法性。
例如输入框要求输入的是数字，当输入了字母是就属于“非法”。
要实现该功能，需要设置 validate、validatecommand 和 invalidcommand 三个选项
"""

#### validate选项可以设置的的值  ####
"""
'focus'   当 Entry 组件获得或失去焦点的时候验证
'focusin'   当 Entry 组件获得焦点的时候验证
'focusout'   当 Entry 组件失去焦点的时候验证
'key'     当输入框被编辑的时候验证
'all'     当出现上面任何一种情况是验证
'none'    关闭验证功能。默认设置该选项（即不开启）。注意是字符串'none', 不是None
"""


# 其次是为 validatecommand 选项指定一个验证函数，该函数只能返回 True 或 False 表示验证结果。
# 一般情况验证函数只需要知道输入框的内容即可，可以通过 Entry 组件的 get() 方法获得该字符串。