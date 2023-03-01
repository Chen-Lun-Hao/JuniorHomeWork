'''
Description: 
Author: Xiao
Date: 2023-02-25 21:38:30
LastEditTime: 2023-03-01 09:19:34
LastEditors: Xiao
'''
# encoding:utf8

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ImageWithMouseControl(QWidget):
    x0=0
    y0=0
    x1=0
    y1=0
    flag=False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap('111.png')
        self.scaled_img = self.img.scaled(self.size())
        self.point = QPoint(0, 0)
        self.Color=Qt.blue#pen color: defult:blue
        self.penwidth=4#pen width : default:4

        self.initUI()

    def initUI(self):
        self.left_click = False
        self.right_click = False
        self.setWindowTitle('Image with mouse control')

    def paintEvent(self, e):
        '''
        绘图
        :param e:
        :return:
        '''
        if self.left_click:
            # 左键
            painter1 = QPainter(self.scaled_img)# 在图片上画
            # painter1.begin(self)
            painter1.setPen(QPen(self.Color,self.penwidth,Qt.SolidLine))
            painter1.drawLine(self.x0,self.y0,self.x1,self.y1)
            self.draw_img(painter1)
            # Label_painter=QPainter(self)
            # Label_painter.drawPixmap(self.point,self.img)
            # painter1.end()
            # Label_painter=QPainter(self)
            # Label_painter.drawPixmap(2,2,self.img)
        elif not self.left_click:
            painter = QPainter()
            painter.begin(self)
            self.draw_img(painter)
            painter.end()

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)

    #鼠标移动事件
    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.left_click:#按住左键移动，绘画
            self.x0 = self.x1
            self.y0 = self.y1
            self.x1 = e.x()
            self.y1 = e.y()
            self.update()
            # self._endPos = e.pos() - self._startPos
            # self.point = self.point + self._endPos
            # self._startPos = e.pos()
            # self.repaint()
        elif self.right_click:#按住右键移动
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()
            
        
    
    #鼠标双击事件
    def mouseDoubleClickEvent(self, e):
        self.point = QPoint(0, 0)
        self.scaled_img = self.img.scaled(self.size())
        self.repaint()

    #鼠标点击事件
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.right_click = False
            self._startPos = e.pos()
        if e.buttons() == Qt.RightButton:
            self.right_click = True
            self.left_click = False
            self._startPos = e.pos()
            

    #鼠标释放事件
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:#左建
            self.left_click = False
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()
        elif e.button() == Qt.MiddleButton:#中建
            self.point = QPoint(0, 0)
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()

        elif e.button() == Qt.RightButton:#右键释放
            self.right_click = False
        #     self.point = QPoint(0, 0)
        #     self.scaled_img = self.img.scaled(self.size())
        #     self.repaint()

    #滚伦事件
    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            # 放大图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()-5, self.scaled_img.height()-5)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 5)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 5)
            self.point = QPoint(new_w, new_h)
            self.repaint()
        elif e.angleDelta().y() < 0:
            # 缩小图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()+5, self.scaled_img.height()+5)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 5)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 5)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    #进入事件
    # def enterEvent(self, a0: QtCore.QEvent) -> None:
    #     return super().enterEvent(a0)

    #离开事件
    # def leaveEvent(self, a0: QtCore.QEvent) -> None:
    #     return super().leaveEvent(a0)

    def resizeEvent(self,e):#设置窗口大小
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()