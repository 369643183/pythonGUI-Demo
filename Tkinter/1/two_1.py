# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-23 20:33:35
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 10:05:25

from Tkinter import *
root = Tk()

# 创建两个列表
li = ['C','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']

# 通过Listbox创建列表组件对象
#Listbox 列表框控件，用来显示一个字符串列表给用户
listb = Listbox(root)
listb2 = Listbox(root)

for item in li:#循环遍历，把li列表中的值逐个赋值给item这个变量
    listb.insert(0,item)#把item插入到listb中的第0个位置
# 还有一种高级点的写法
# for i in range(20):
#     listb.insert(END, str(i))#把列表中的值添加到末尾(关键字END)

for item in movie:
    listb2.insert(0,item)

#将小部件放置到主窗口中
listb.pack()
listb2.pack()

# 让主窗口工作起来
root.mainloop()