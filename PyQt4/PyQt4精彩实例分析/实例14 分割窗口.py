# -*- coding: utf-8 -*-

# http://www.linuxidc.com/Linux/2012-06/63652p14.htm

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWidget(QMainWindow):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)

        # 指定显示的字体
        font=QFont(self.tr("黑体"),12)
        QApplication.setFont(font)

        # 定义一个QSplitter类对象，为主分割窗口，设定此分割窗为水平分割窜
        mainSplitter=QSplitter(Qt.Horizontal,self)

        # 定义一个QTextEdit类对象，并插入主分割窗口中
        leftText=QTextEdit(self.tr("左窗口"),mainSplitter)

        # 调用setAlignment()方法，设定TextEdit中文字的对齐方式
        leftText.setAlignment(Qt.AlignCenter)

        # 定义一个右部的分割窗口，定义为垂直分割窗，并以主分割窗口为父窗口。
        rightSplitter=QSplitter(Qt.Vertical,mainSplitter)

        # 调用的方法setOpaqueResize(boolean)用由设定分割窗的分割条在拖动时是否为实时更新显示，若设为True则实时更新显示，若设为False则在拖动时只显示一条灰色的精线条，在拖动到位并弹起鼠标后再显示分割条。默认设为True，这和Qt3正好相反，Qt3中默认为False。
        rightSplitter.setOpaqueResize(False)

        upText=QTextEdit(self.tr("上窗口"),rightSplitter)
        upText.setAlignment(Qt.AlignCenter)
        bottomText=QTextEdit(self.tr("下窗口"),rightSplitter)
        bottomText.setAlignment(Qt.AlignCenter)

        # setStretchFactor()方法用于设定可伸缩控件，它的第一个参数指定设置的控件序号，控件序号按插入的先后次序从0起依次编号，第二个参数大于0的值表示此控件为可伸缩控件。此实例中设定右部分割窗为可伸缩控件，当整个对话框的宽度发生改变时，左部的文件编辑框宽度保持不变，右部的分割窗宽度随整个对话框大小的改变进行调整。
        mainSplitter.setStretchFactor(1,1)

        mainSplitter.setWindowTitle(self.tr("分割窗口"))

        self.setCentralWidget(mainSplitter)

app=QApplication(sys.argv)
main=MainWidget()
main.show()
app.exec_()

# setAlignment()方法，设定TextEdit中文字的对齐方式，常用的有以下几种。

# Qt.AlignLeft：左对齐。

# Qt.AlignRight：右对齐。

# Qt.AlignCenter：文字居中(Qt.AlignHCenter为水平居中，Qt.AlignVCenter为垂直居中)。

# Qt.AlignUp：文字与顶端对齐。

# Qt.AlignBottom：文字与底部对齐。


