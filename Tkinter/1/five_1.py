# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-24 11:08:10
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-24 11:55:47

# 根据单选按钮来切换文字的颜色，并根据输入改变文字的内容
# http://www.jianshu.com/p/5c7a1af4aa53


from Tkinter import *

class ChangeLabelDemo:
    def __init__(self):

        window = Tk()
        #window = Tk(className="标题")
        window.title = "改变labeldemo"#这一行是设置窗口标题？为什么没有效果？？？

        # Frame 框架控件；在屏幕上显示一个矩形区域，多用来作为容器
        frame1= Frame(window)
        frame1.pack()
        # Label 标签控件；可以显示文本和位图
        self.lb1 = Label(frame1, text = "Programming is fun")
        self.lb1.pack()
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "输入")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "改变text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg="red",variable=self.v1,value="R",command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text="Yellow", bg="yellow", variable=self.v1, value="Y", command=self.processRadiobutton)

        # 网格布局（grid网格管理器）设置部件的的网格坐标
        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop()

    def processButton(self):
        self.lb1["text"] = self.msg.get()
    def processRadiobutton(self):
        if self.v1.get() == "R":
            self.lb1["fg"] = "red"
        elif self.v1.get() == "Y":
            self.lb1["fg"] = "yellow"
ChangeLabelDemo()