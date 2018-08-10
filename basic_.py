#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  2018-8-10

@author: lilinze
"""
'''
# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出
'''
# s = "hello world"
# s1 = sorted(s)
# s2 = ''.join(s1)
# print(s1)
# print(s2)

'''
# 问题二：数值比较

n = [9,15,23,89,33,26,2,76]

# 请编写代码，找出数组中的最大数与最小数
'''
# max()  min()
# n = [9,15,23,89,33,26,2,76]
# max = n[0]
# min = n[0]
# for i in range(len(n)):
#     if n[i] > max:
#         max = n[i]
#
#     elif n[i] < min:
#         min = n[i]
#
# print('max:',max,'min:',min)

'''
# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子
'''
a = "i,am,a,student,in,chengdu"
i = input('input1:')
j = input('input2:')
a1 = a[0:7]
a2 = a[14:18]
new_a = a1+i+a2+j
print(new_a)








