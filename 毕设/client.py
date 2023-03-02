'''
Description: 
Author: Xiao
Date: 2023-03-01 09:38:20
LastEditTime: 2023-03-01 13:41:08
LastEditors: Xiao
'''
#项目主入口
from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import QApplication

from widgets.MyTitle import TitleWindow
from settings import *
from ui.ImageHandleToCanvas import MyMian


if __name__ == "__main__":
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = TitleWindow(widget_2_sub=MyMian())#主窗口控件，图标路径，标题
    myWin.show()
    sys.exit(app.exec_())