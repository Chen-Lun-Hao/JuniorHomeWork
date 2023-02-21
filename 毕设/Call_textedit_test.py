'''
Description: 
Author: Xiao
Date: 2023-02-21 08:57:17
LastEditTime: 2023-02-21 08:58:21
LastEditors: Xiao
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：mgboy time:2020/7/26
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog
from PyQt5 import QtCore

from textedit_test import Ui_Form
from CallTitleTest import TitleWindow

class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_text)
        self.lineEdit.returnPressed.connect(self.show_text)
        self.lineEdit.setPlaceholderText('请输入字符串')
        self.lineEdit.setClearButtonEnabled(True)
        qss = '''
        QPushButton#pushButton{
        width:30px;
        height:15px;
        border-radius:5px;
        background-color:gray;
        }
        '''
        self.setStyleSheet(qss)

    def show_text(self):
        text = '输入了：' + self.lineEdit.text()
        self.textEdit.insertPlainText(text)

    def returnPressed_func(self):
        current_text = self.lineEdit.text()
        print("文本框回车键信号", current_text)
        self.textBrowser.append("文本框回车键信号" + current_text + '\n'+ '\n' + '回车键')

if __name__ == "__main__":
    #适配2k等高分辨率屏幕
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = TitleWindow(widget_2_sub=MyWindow(),icon_path=None,title='OmyG')
    myWin.show()
    sys.exit(app.exec_())
