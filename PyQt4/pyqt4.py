# -*- coding: utf-8 -*-

# python3

import sys
from PyQt4 import QtGui #引入的QtGui是PyQt中最基本的模块，包含了PyQt的绘图组件及其相关类

# 使用QApplication创建了一个application。每个PyQt程序中均要包含一个application对象。
app = QtGui.QApplication(sys.argv)

# 使用QWidget创建了一个widget
widget = QtGui.QWidget()

# 使用resize设置了widget的大小
widget.resize(250, 150)

# 设置了窗口标题的文字
widget.setWindowTitle('PyQt')

# 使这个widget显示出来
widget.show()

# 程序的主循环，事件处理从本行语句开始。
sys.exit(app.exec_())