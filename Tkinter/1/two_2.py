# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 09:23:51
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 11:07:21

from Tkinter import *

root = Tk()

# 这个列表默认只会展示10行（超过的部分可滚动显示），当用户拖拽放大窗口的时候，Tkinter将会增加包裹列表的内边距，而不会放大列表本身
# listbox = Listbox(root)
# listbox.pack()
# 若要列表装满父容器，并且用户可以手动拖拽容器来放大列表，可以使用fill和expand选项来实现。
# listbox.pack(fill=BOTH, expand=1)
# fill：填充这整个空间，并指定包管理器这个小构件（widget）的填充方式
# BOTH：指定这个构件在水平和垂直两个方向伸展，X在水平方向伸展，Y在竖直方向伸展。
# expand：当值非0时，是告诉包管理器分配额外的空间给构件，当父容器足够包裹所有的子构件时，多于的扩展空间就会填充在构件之间

for i in range(20):
    listbox.insert(END, str(i))

mainloop()
