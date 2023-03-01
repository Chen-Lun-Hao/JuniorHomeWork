'''
Description: 
Author: Xiao
Date: 2023-03-01 09:38:20
LastEditTime: 2023-03-01 09:38:30
LastEditors: Xiao
'''
#项目主入口
from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import QApplication
from TitleEdit import TitleWindow


if __name__ == "__main__":
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = TitleWindow()
    myWin.show()
    sys.exit(app.exec_())