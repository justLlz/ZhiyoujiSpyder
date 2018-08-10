#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2018-8-10

@author: lilinze
"""
'''
# 使用 while 循环打印 1 3 5 7 9

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1,5,7,8,9]

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"

'''
# 使用 while 循环打印 1 3 5 7 9
# i = 1
# num = 6
# while i < num:
#       print(2*i-1)
#       i += 1


# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”


# def found(num,l):
#     if num in l:
#         print('found')
#     else:
#         print('not found')
#
# l = [1,5,7,8,9]
# num = 6
# found(num,l)

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"
s_ = sorted(s)
s1 = ''.join(s_[7::]).lower()
s2 = ''.join(s_[0:7])
print(s1)
print(s2)



















