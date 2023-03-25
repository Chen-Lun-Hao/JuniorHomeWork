'''
Description:图像格式转换
Author: Xiao
Date: 2023-02-25 21:38:30
LastEditTime: 2023-03-25 13:29:32
LastEditors: Xiao
'''
import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import qDebug
import numpy as np
from PIL import ImageQt

#opencv转为qpixmap
def Opencv_to_QPixmap(img):
    # 通道转化  BGR->RGB
    RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 将图片转化成Qt可读格式   QImage
    qimage = QImage(RGBImg, RGBImg.shape[1], RGBImg.shape[0], QImage.Format_RGB888)
    piximage = QPixmap(qimage)
    return piximage
    

# QPixmap 转为 CV2
def Pixmap_to_Opencv(img):
    qimg = img.toImage()  # QPixmap-->QImage

    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]#此处为BGR格式
    # cv2.imwrite('./result.jpg',result) # 保存的话会显示RGB格式
    return result



# QImage 转为 Opencv
def QImage_to_Opencv(img):
    tmp = img
    # 使用numpy创建空的图象
    cv_image = np.zeros((tmp.height(), tmp.width(), 3), dtype=np.uint8)
    print('begin cv_image type:',type(cv_image))
    for row in range(0, tmp.height()):
        for col in range(0, tmp.width()):
            r = qRed(tmp.pixel(col, row))
            g = qGreen(tmp.pixel(col, row))
            b = qBlue(tmp.pixel(col, row))
            cv_image[row, col, 0] = b
            cv_image[row, col, 1] = g
            cv_image[row, col, 2] = r
    return cv_image


# opencv 转为 Qimage 
def CV2QImage(cv_image):
    
    width = cv_image.shape[1] #获取图片宽度
    height = cv_image.shape[0]  #获取图片高度
    
    pixmap = QPixmap(width, height) #根据已知的高度和宽度新建一个空的QPixmap,
    qimg = pixmap.toImage()  #将pximap转换为QImage类型的qimg
    
    #循环读取cv_image的每个像素的r,g,b值，构成qRgb对象，再设置为qimg内指定位置的像素
    for row in range(0, height):
        for col in range(0,width):
            b = cv_image[row,col,0]
            g = cv_image[row,col,1]
            r = cv_image[row,col,2]
            
            pix = qRgb(r, g, b)
            qimg.setPixel(col, row, pix)
    
    return qimg #转换完成，返回
    
#PIL格式转QPixmap格式
def pilimg_to_qtpixmap(pilimg):
    pilimg = np.asarray(pilimg)
    #opencv转为qimage
    height, width, depth = pilimg.shape#一般使用rgb三通道
    # pilimg = cv2.cvtColor(pilimg, cv2.COLOR_BGR2RGB)
    pilimg = QImage(pilimg.data, width, height, width * depth, QImage.Format_RGB888)
    pilimg = QPixmap.fromImage(pilimg)
    return pilimg
 
#QPixmap格式转PIL格式
def pixmap2_pil(img):
    img_obj = ImageQt.fromqpixmap(img)
    return  img_obj