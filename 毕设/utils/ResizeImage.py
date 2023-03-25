'''
Description: 对图片进行无损缩放，三通道或者四通道，RGB或者RGBA
Author: Xiao
Date: 2023-03-22 23:12:13
LastEditTime: 2023-03-22 23:30:27
LastEditors: Xiao
'''
from PIL import Image
import time

def letterbox_image(image, scale):
    #Image类型的图片以及缩放倍数
    iw, ih = image.size
    # w, h = size
    # scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    size = (nw, nh)

    image = image.resize((nw, nh), Image.BICUBIC)
    # new_image = Image.new('RGB', size, (128, 128, 128))
    # new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    return image#rgb格式

