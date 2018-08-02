# -*- coding: utf-8 -*-
# @Author: zhq
# @Date:   2018-04-05 19:34:41
# @Last Modified by:   zhq
# @Last Modified time: 2018-04-05 19:45:13

import easygui as g
import sys

g.msgbox("欢迎进入第一个小界面游戏")
title = "小游戏互动"
choices = ['java', 'python', 'javascript', 'php', 'jsp', 'asp']
msg = "你在学哪种编程语言呢？"
choice = g.choicebox(msg, title, choices)

g.msgbox("你选择的是：" + str(choice), "结果")
msg = "你希望重新开始小游戏吗？"
title = "请选择"

if g.ccbox(msg, title):
    pass
else:
    sys.exit(0)