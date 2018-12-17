#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')

name = input()
print('Hello,', name)

#split函数分割，eval转换字符为数值型
math = input('please enter your math function:\n \t Example:\n\t 100.12*5.2\n')
numbers = math.split('*')
first = eval(numbers[0])
second = eval(numbers[1])
print(first,'*',second,'=',first*second)
