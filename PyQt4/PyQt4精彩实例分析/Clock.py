# -*- coding: utf-8 -*-

# 本实例实现一个数字电子钟程序，显示于桌面上，并可随意拖动至桌面任意位置。
# http://www.linuxidc.com/Linux/2012-06/63652p14.htm
# https://segmentfault.com/a/1190000005165656

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class DigiClock(QLCDNumber):
    def __init__(self,parent=None):
        super(DigiClock,self).__init__(parent)

        p=self.palette()
        p.setColor(QPalette.Window,Qt.blue)
        self.setPalette(p)

        self.dragPosition=None

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)

        timer=QTimer(self)
        self.connect(timer,SIGNAL("timeout()"),self.showTime)
        timer.start(1000)

        self.showColon=True
        self.showTime()
        self.resize(150,60)

    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
            event.accept()
        if event.button()==Qt.RightButton:
            self.close()

    def mouseMoveEvent(self,event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos()-self.dragPosition)
            event.accept()

    def showTime(self):
        time=QTime.currentTime()
        text=time.toString("hh:mm")
        if self.showColon:
            text.replace(2,1,":")
            self.showColon=False
        else:
            text.replace(2,1," ")
            self.showColon=True
        self.display(text)

app=QApplication(sys.argv)
form=DigiClock()
form.show()
app.exec_()