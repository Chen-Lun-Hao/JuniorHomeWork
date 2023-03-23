'''
Description: 
Author: Xiao
Date: 2023-03-02 12:42:33
LastEditTime: 2023-03-02 12:44:24
LastEditors: Xiao
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：mgboy time:2020/6/25
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ui.Ui_Imagehandle import Ui_Form
from widgets.MyCanvas import ImageWithMouseControl

class MyMian(QWidget,Ui_Form):
    def __init__(self):
        super(MyMian, self).__init__()
        self.setupUi(self)
        # pix = QPixmap('111.png')
        self.w = ImageWithMouseControl(self.widget)#,'毕设/my.jpg')
        self.w.setGeometry(10, 10, 600, 600)#设置大小
    
    def my_Qss(self):
        # 给标题栏控件设置别的属性名，这样就不会在美化时和新加进来的内容栏窗口的控件有冲突了
        self.label.setProperty('other_name', 'ImageDisplay')#图片显示窗口
        self.widget.setProperty('other_name', 'Edit_widget')#编辑区域窗口
        self.pushButton.setProperty('other_name', 'Painting_button')#笔刷按钮
        self.pushButton_2.setProperty('other_name', 'Color_button')#颜色选择按钮
        self.pushButton_3.setProperty('other_name', 'Abrasion_button')#擦除按钮
        self.widget_2.setProperty('other_name', 'Layout_widget')#图层区域窗口