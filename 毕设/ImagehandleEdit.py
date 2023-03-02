'''
Description: 
Author: Xiao
Date: 2023-02-25 14:37:23
LastEditTime: 2023-03-02 12:35:39
LastEditors: Xiao
'''

# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog
from PyQt5 import QtCore

from ui.Ui_Imagehandle import Ui_Form

class ImageWindow(QWidget, Ui_Form):
    def __init__(self):
        super(ImageWindow, self).__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 1
 
    def init_ui(self):
        self.setWindowTitle("ImageBox")
    
    def my_Qss(self):
        # 给标题栏控件设置别的属性名，这样就不会在美化时和新加进来的内容栏窗口的控件有冲突了
        self.label.setProperty('other_name', 'ImageDisplay')#图片显示窗口
        self.widget.setProperty('other_name', 'Edit_widget')#编辑区域窗口
        self.pushButton.setProperty('other_name', 'Painting_button')#笔刷按钮
        self.pushButton_2.setProperty('other_name', 'Color_button')#颜色选择按钮
        self.pushButton_3.setProperty('other_name', 'Abrasion_button')#擦除按钮
        self.widget_2.setProperty('other_name', 'Layout_widget')#图层区域窗口
