# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2017-09-26 21:12:54
# @Last Modified by:   zhq
# @Last Modified time: 2017-09-27 18:54:05

import easygui as g
import sys

g.msgbox("第一个界面小游戏")
msg = "请选择编程语言"
title = "这是标题"
choices = ["C","Python","Java","PHP"]
choice = g.choicebox(msg,title,choices)


g.msgbox("你的选择是：" + str(choice),"结果")
msg = "是否重新开始游戏？"

title = "请选择"
if g.ccbox(msg,title):
    pass
else:
    sys.exit(0)