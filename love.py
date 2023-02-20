'''
Description: 
Author: Xiao
Date: 2023-02-04 14:45:23
LastEditTime: 2023-02-04 23:10:22
LastEditors: Xiao
'''
import turtle
import time
# # 清屏函数
# def clear_all():
#     turtle.penup()
#     turtle.goto(0, 0)
#     turtle.color('white')
#     turtle.pensize(800)
#     turtle.pendown()
#     turtle.setheading(0)
#     turtle.fd(300)
#     turtle.bk(600)

# # 重定位海龟的位置
# def go_to(x, y, state):
#     turtle.pendown() if state else turtle.penup()
#     turtle.goto(x, y)

# # 画爱心
# def draw_heart(size):
#     turtle.color('red', 'red')
#     turtle.pensize(2)
#     turtle.penup()
#     turtle.pendown()
#     turtle.setheading(150)
#     turtle.begin_fill()
#     turtle.fd(size)
#     turtle.circle(size * -3.745, 45)
#     turtle.circle(size * -1.431, 165)
#     turtle.left(120)
#     turtle.circle(size * -1.431, 165)
#     turtle.circle(size * -3.745, 45)
#     turtle.fd(size)
#     turtle.end_fill()


# def main():
#     turtle.setup(900, 500)
#     # turtle.speed(10)
#     draw_heart(14)
#     # clear_all()
#     turtle.done()

# main()


import turtle
import random
import math
 
# 初始化
turtle.setup(1280, 720)
t = turtle.Pen()
t.ht()
 
# 颜色
colors = []
t_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
 
for i in t_list:
    t_str = "#ff00"
    for j in t_list:
        colors.append(t_str+i+j)
 
 
class Love():
    def __init__(self):
        # 定义变量
        self.r = random.randint(4, 10)
        self.x = random.randint(-900, 700)
        self.y = random.randint(-400, 400)
        self.i = random.randint(0, 10)
        self.color = random.choice(colors)
        self.speed = random.randint(1, 8)
    
    def move(self):
        # 通过y坐标来控制爱心
        if self.y <= 500:
            self.y += 2.5*self.speed
            self.x = self.x + 1.5*math.sin(self.i)*math.sqrt(self.i)*self.speed
            self.i = self.i + 0.1
        else:
            self.y = -700
            self.r = random.randint(5, 20)
            self.x = random.randint(-900, 700)
            self.i = 0
            self.color = random.choice(colors)
            self.speed = random.randint(1, 8)
 
    def draw(self, size):
        # 绘制爱心
        t.pensize(self.r/2)
        t.penup()
        t.color('red', 'red')
        t.goto(100, 100)
        t.pendown()
        t.begin_fill()
        t.fillcolor('red')
        # 设置角度
        t.setheading(60)
        t.circle(size, 255)
        t.fd(2*size)
        t.left(90)
        t.fd(2*size)
        t.circle(size, 255)
        t.end_fill()

#     turtle.fd(size)
#     turtle.circle(size * -3.745, 45)
#     turtle.circle(size * -1.431, 165)
#     turtle.left(120)
#     turtle.circle(size * -1.431, 165)
#     turtle.circle(size * -3.745, 45)
#     turtle.fd(size)
 
love = []
# for i in range(100):
love.append(Love())

Resize = [i for i in range(100)]
 
for i in range(100):
    turtle.tracer(0)
    t.clear()
    # for i in range(80):
    # love[0].move()
    love[0].draw(i)
    turtle.tracer(1)
    time.sleep(0.01)
love[0].draw(99)