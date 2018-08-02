# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-07 21:08:48
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 10:30:49

# 通过 Tab 键将焦点转移到第二个输入框时，触发验证功能


from tkinter import *

root = Tk()

def test1():
    if e1.get() == "luck":
        print("正确")
        return True
    else:
        print("错误")
        e1.delete(0, END)
        return False

def test2():
    print("成功被调用")
    return True

v = StringVar()
# e1 = Entry(root, textvariable = v, validate = "focusout", validatecommand = test1)
e1 = Entry(root, textvariable = v, validate = "focusout", validatecommand = test1, invalidcommand = test2)
e2 = Entry(root)
e1.pack(padx = 20, pady = 20)
e2.pack(padx = 20, pady = 20)

mainloop()


######## Tkinter 为验证函数提供一额外的选项 ########
"""
'%d'        操作代码：0表示删除；1表示插入操作；2表示获得、失去焦点或 textvariable 变量的值被修改

'%i'        当用户尝试插入或删除操作的时候，该选项表示插入或删除的位置（索引号）
            如果时由于获得、失去焦点或 textvariable 变量的值被修改而调用验证函数，那么该值时-1

'%P'        当输入框的值允许改变时，该值有效
            该值为输入框的最新文本内容

'%s'        该值调用验证函数前输入框的内容

'%S'        当插入或删除操作触发验证函数时，该值有效
            该选项表示文本被插入和删除的内容

'%v'        该组件当前的 validate 选项的值

'%V'        调用该函数的原因
            该值时'focusout', 'focusin', 'key' 或 'forced'（textvariable选项指定的变量值被修改）中的一个

'%W'        该组件的名字
"""

"""
为了使用这些选项，可以这样写：
    validatecommand = (f, s1, s2, ...)
其中，f 是验证函数名， s1、s2、s3是额外的选项，这些选项作为参数依次传递给 f 函数。
在此之前，需要调用 register() 方法将验证函数包装起来:
"""