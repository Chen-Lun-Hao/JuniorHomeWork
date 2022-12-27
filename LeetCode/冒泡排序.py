'''
Description: 
Author: Xiao
Date: 2022-12-27 12:47:32
LastEditTime: 2022-12-27 13:32:53
LastEditors: Xiao
'''
# 对列表[3,1,4,5,9,6,8,2,7]排序

def MaoPao(input):#每次循环最大的都减少了
    for i in range(len(input)):
        for j in range(len(input)-1-i):
            if input[j] > input[j+1]:
                t = input[j]
                input[j] = input[j+1]
                input[j+1] = t
    print(input)
    return input

tl = [3,1,4,5,9,6,8,2,7]
print(tl)
tl = MaoPao(tl)
        