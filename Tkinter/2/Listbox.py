# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-08 20:08:49
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-08 20:34:10

"""
创建一个 Listbox 组件时，里面是空的。
所以，需要使用 insert() 方法添加文本，
该方法有两个参数：
第一个是插入的索引号（也就是序号，第一项是0）
第二个是插入的字符串
"""

from tkinter import *
root = Tk()
# 创建一个空列表
theLB = Listbox(root, setgrid = True)
theLB.pack()
# 往列表里添加数据
for item in ['apple', 'banana', 'paer', 'orange']:
    theLB.insert(END,item)

theButton = Button(root, text = "删除", command = lambda x = theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()

"""
使用 delete()方法删除列表中的项目，最常用的操作是删除列表中的所有项目：listbox.delete(0, END)
也可以删除指定项目，添加加一个独立的按钮来删除 ACTIVE 状态的项目：

# 跟 END 一样，这个 ACTIVE 是一个特殊的索引号，表示当前被选中的项目
theButton = Button(master, text = "删除", command = lambda x = theLB: x.delete(ACTIVE))
theButton.pack()

Listbox 组件根据 selectmode 选项提供了4种不同的选择模式：
    SINGLE 单选
    BROWSE （默认的值）单选，但拖动鼠标或通过方向键可以直接改变选项
    MULTIPLE 多选
    EXTENDED 多选，但需要同时按住 Shift 或 Ctrl 或拖动鼠标实现
"""