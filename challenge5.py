#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: challenge5.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 6月 01, 2020
# ---
import operator

I = {1: 2, 3: 4, 4:3, 2:1, 0:0}

sorted_I = sorted(I.items(), key=operator.itemgetter(0))
print(sorted_I)