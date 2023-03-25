

'''
Description: 
Author: Xiao
Date: 2023-02-25 21:38:30
LastEditTime: 2023-03-25 22:57:57
LastEditors: Xiao
'''
# encoding:utf8

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import utils.ResizeImage as ri#缩放图片
import utils.Image_conversion as iv
from PIL import Image

class MyCanvas(QWidget):

    def __init__(self, parent=None, img=None, pen=None, layer=None):
        super(MyCanvas, self).__init__(parent)
        self.parent = parent# 父控件
        self.img = img#PIL类型
        self.pen = pen#绘制所用的笔类型，QPainter
        self.layer = layer#位于第layer层

        iw, ih = self.img.size#读取的图片尺寸
        fw, fh = self.parent.width(), self.parent.height()#父控件大小
        scale = min(fw/iw, fh/ih)#比例最小那个
        self.img = ri.letterbox_image(self.img, scale=scale)#缩放
        self.img = iv.pilimg_to_qtpixmap(self.img)#转为qpixmap

        self.point = QPoint(0, 0)#当前角点

        self.initUI()


    def initUI(self):#变量初始化
        self.left_click = False
        self.right_click = False
        self.setWindowTitle('Image with mouse control')

    def paintEvent(self, e):
        #绘图事件
        #绘图时必须使用QPainter的实例，此处为__painter
        #绘图在begin()函数与end()函数间进行
        #begin(param)的参数要指定绘图设备，即把图画在哪里
        #drawPixmap用于绘制QPixmap类型的对象
        if self.left_click:
            # 左键绘画
            # painter = QPainter(self.img)
            self.pen.begin(self)
            self.pen.setPen(QPen(self._penColor,self._thickness))
            self.pen.drawLine(self._lastPos, self._currentPos)
            self.pen.end()
            
        # elif not self.left_click:
        # painter = QPainter()
        self.pen.begin(self)
        self.pen.drawPixmap(self.point, self.img)#从point绘制图像
        self.pen.end()
        

    

    
    def mouseMoveEvent(self, e):#重写移动事件
        
    

    #     self.img = QPixmap('my.jpg')#相当与画板
    #     self.scaled_img = self.img.scaled(self.size())#相当与画板

    #     self.point = QPoint(0, 0)#当前角点

    #     self._startPos = QPoint(0, 0)#起始位置
    #     self._lastPos = QPoint(0,0)#上一次鼠标位置
    #     self._currentPos = QPoint(0,0)#当前的鼠标位置
    #     self._thickness = 4       #默认画笔粗细为4px
    #     self._penColor = QColor("blue")#设置默认画笔颜色为黑色
    #     self.flag = False#是否绘画
    #     #右键鼠标后的偏移量(左负右正)，同时，在图像之外的不能绘画

    #     self.initUI()

    # def initUI(self):
    #     self.left_click = False
    #     self.right_click = False
    #     self.setWindowTitle('Image with mouse control')

    # def paintEvent(self, e):
    #     #绘图事件
    #     #绘图时必须使用QPainter的实例，此处为__painter
    #     #绘图在begin()函数与end()函数间进行
    #     #begin(param)的参数要指定绘图设备，即把图画在哪里
    #     #drawPixmap用于绘制QPixmap类型的对象
    #     if self.left_click:
    #         # 左键
    #         painter = QPainter(self.scaled_img)
    #         painter.setPen(QPen(self._penColor,self._thickness))
    #         painter.drawLine(self._lastPos, self._currentPos)
            
    #     # elif not self.left_click:
    #     painter = QPainter()
    #     painter.begin(self)
    #     self.draw_img(painter)
    #     painter.end()


    # #鼠标移动事件
    # def mouseMoveEvent(self, e):  # 重写移动事件
    #     if self.left_click:#按住左键移动，绘画
    #         self.flag = True#绘画标志
    #         #鼠标移动时，更新当前位置，并在上一个位置和当前位置间画线
    #         self._lastPos =  self._currentPos#记录当前位置
    #         self._currentPos = e.pos() - self.point#防止右键移动时，绘画发生偏移
    #         self.update()
    #     elif self.right_click:#按住右键移动
    #         self._endPos = e.pos() - self._startPos#偏移量
    #         print(self._endPos)
    #         self.point = self.point + self._endPos#左上角的点也改变
    #         self._startPos = e.pos()
    #         self.repaint()
            
        
    
    # #鼠标双击事件
    # def mouseDoubleClickEvent(self, e):
    #     self.point = QPoint(0, 0)
    #     self.scaled_img = self.scaled_img.scaled(self.size())
    #     self.repaint()

    # #鼠标点击事件
    # def mousePressEvent(self, e):
    #     if e.button() == Qt.LeftButton:#开始绘画
    #         self.left_click = True
    #         self.right_click = False
    #         self._currentPos = e.pos() - self.point#防止右键移动时，绘画发生偏移,绘画开始位置
    #     if e.buttons() == Qt.RightButton:#开始移动
    #         self.right_click = True
    #         self.left_click = False
    #         self._startPos = e.pos()
            

    # #鼠标释放事件
    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.LeftButton:#左建
    #         self.left_click = False
    #         # self.scaled_img = self.img.scaled(self.size())
    #     elif e.button() == Qt.MiddleButton:#中建
    #         self.point = QPoint(0, 0)
    #         if self.flag:
    #             self.scaled_img = self.scaled_img
    #         else:
    #             self.scaled_img = self.img.scaled(self.size())
    #         self.repaint()

    #     elif e.button() == Qt.RightButton:#右键释放
    #         self.right_click = False


    # #滚伦事件
    # def wheelEvent(self, e):
    #     if e.angleDelta().y() > 0:
    #         # 放大图片
    #         self.scaled_img = self.img.scaled(self.scaled_img.width()-5, self.scaled_img.height()-5)
    #         new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 5)
    #         new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 5)
    #         self.point = QPoint(new_w, new_h)
    #         self.repaint()
    #     elif e.angleDelta().y() < 0:
    #         # 缩小图片
    #         self.scaled_img = self.img.scaled(self.scaled_img.width()+5, self.scaled_img.height()+5)
    #         new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 5)
    #         new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 5)
    #         self.point = QPoint(new_w, new_h)
    #         self.repaint()

    # #进入事件
    # # def enterEvent(self, a0: QtCore.QEvent) -> None:
    # #     return super().enterEvent(a0)

    # #离开事件
    # # def leaveEvent(self, a0: QtCore.QEvent) -> None:
    # #     return super().leaveEvent(a0)

    # def resizeEvent(self,e):#设置窗口大小
    #     if self.parent is not None:
    #         self.scaled_img = self.img.scaled(self.size())
    #         self.point = QPoint(0, 0)
    #         self.update()

