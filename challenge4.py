#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: challenge4.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 6月 01, 2020
# ---


def func(x):
    if x <= 100000:
        a = x * 0.1
        return a
    elif 200000>= x >100000:
        b = 10000 + (x-100000)*0.075
        return b
    elif 400000>= x > 200000:
        c = 17500 + (x-200000)*0.05
        return  c

I= int(input('净利润：'))
profit = func(I)
print('利润为%d元时， 应发奖金总数为%d元' % (I, profit))

