'''
Description: 
Author: Xiao
Date: 2023-02-25 21:38:30
LastEditTime: 2023-03-04 01:11:14
LastEditors: Xiao
'''
# encoding:utf8

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ImageWithMouseControl(QWidget):
    
    def __init__(self, parent=None,imgpath=None):
        '''
        parent: 父类
        imgpath: 图片路径
        '''
        super().__init__(parent)
        self.parent = parent
        self.img = QPixmap(imgpath)
        self.scaled_img = self.img.scaled(self.size())#缩放，返回一个新的qpixmap
        self.point = QPoint(0, 0)#定义了一个整形精度的点
        self.pen = QPainter()#绘图工具
        self.Color=Qt.blue#pen color: defult:blue画笔为蓝色
        self.penwidth=4#pen width : default:4笔触是4
        self.pen.setPen(QPen(self.Color,self.penwidth))#设置画笔颜色与粗细

        self.initUI()

    def initUI(self):
        #初始化
        self.left_click = False
        self.right_click = False
        self.setWindowTitle('Image with mouse handle')

    def paintEvent(self, e):
        #绘图事件
        #绘图时必须使用QPainter的实例，此处为__painter
        #绘图在begin()函数与end()函数间进行
        #begin(param)的参数要指定绘图设备，即把图画在哪里
        #drawPixmap用于绘制QPixmap类型的对象
        if self.left_click:
            # 左键，在图片上画画
            self.pen = QPainter(self.scaled_img)# 在图片上画
            self.pen.setPen(QPen(self.Color,self.penwidth,Qt.SolidLine))
            self.pen.drawLine(self.x0,self.y0,self.x1,self.y1)
            self.pen.begin(self)#paintevent开始执行
            self.draw_img(self.pen)
            self.pen.end()#结束
        elif not self.left_click:
            painter = QPainter()
            painter.begin(self)
            self.draw_img(painter)
            painter.end()

    def draw_img(self, painter):# 绘制QPixmap的图片
        painter.drawPixmap(self.point, self.scaled_img)

    #鼠标点击事件
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.right_click = False
            self._startPos = e.pos()#绘画鼠标开始位置
        if e.buttons() == Qt.RightButton:
            self.right_click = True
            self.left_click = False
            self._startPos = e.pos()#移动鼠标开始位置

    #鼠标移动事件
    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.left_click:#按住左键移动，绘画
            #鼠标移动时，更新当前位置，并在上一个位置和当前位置间画线
            self.__currentPos =  e.pos()#记录当前位置
            self.pen.begin(self.scaled_img)
            self.pen.drawLine(self._startPos, self.__currentPos)
            self.pen.end()
            self._startPos = self.__currentPos#更新开始位置
            self.update() #更新显示
        elif self.right_click:#按住右键移动
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos#计算鼠标移动到哪里
            self._startPos = e.pos()#鼠标位置
            self.repaint()
            
        
    
    #鼠标双击事件，鼠标复位
    def mouseDoubleClickEvent(self, e):
        #从左上角开始绘画
        self.point = QPoint(0, 0)
        self.scaled_img = self.img.scaled(self.size())
        self.repaint()

    
            

    #鼠标释放事件
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:#左建
            self.left_click = False
            # self.scaled_img = self.img.scaled(self.size())
            # self.repaint()
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