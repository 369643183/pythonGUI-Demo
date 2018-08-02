# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
# root = Tk(className='标题')

# 构件默认是在主窗口中居中按照一列排序

w = Label(root, text="Red", bg="red", fg="white")
w.pack()
w = Label(root, text="Green", bg="green", fg="black")
w.pack()
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack()

w = Label(root, text="添加了fill=X后", bg="Yellow", fg="black")
# 当添加了fill=X后，就可以使构件和父容器一样宽
w.pack(fill=X)

w = Label(root, text="设置side=RIGHT", bg="Black", fg="white")
# 使构件和父容器一样高,并贴近右边
w.pack(fill=Y,side=RIGHT)
# 注意：若只写一个fill=Y的话没有效果，相当于没写。
# side设置构件贴近左边（LEFT）右边（RIGHT）上面（TOP）底部（TOTTOM）

mainloop()