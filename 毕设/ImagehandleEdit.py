'''
Description: 
Author: Xiao
Date: 2023-02-25 14:37:23
LastEditTime: 2023-02-25 16:26:35
LastEditors: Xiao
'''

# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPoint, Qt, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog
from PyQt5 import QtCore

from Ui_Imagehandle import Ui_Form

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


    def wheelEvent(self, event):#使用滚轮实现图片的放大显示
        if event.x() < 0 and event.y() < 0:#判断鼠标是否在label中
            
            return
        

    def set_image(self, img_path):
        """
        open image file
        :param img_path: image file path
        :return:
        """
        # img = QImageReader(img_path)
        # img.setScaledSize(QSize(self.size().width(), self.size().height()))
        # img = img.read()
        self.img = QPixmap(img_path)
        self.scaled_img = self.img
        self.update()
 
    def paintEvent(self, e):
        """
        receive paint events
        :param e: QPaintEvent
        :return:
        """
        if self.scaled_img:
            painter = QPainter()
            painter.begin(self)
            painter.scale(self.scale, self.scale)
            painter.drawPixmap(self.point, self.scaled_img)
            painter.end()
 
    def wheelEvent(self, event):
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()
        # 获取当前鼠标相对于view的位置
        if angleY > 0:
            self.scale *= 1.1
        else:  # 滚轮下滚
            self.scale *= 0.9
        self.adjustSize()
        self.update()
 
 
    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()
 
    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()
 
    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = False