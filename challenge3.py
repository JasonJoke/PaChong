#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: challenge3.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 6月 01, 2020
# ---

for a in range(1, 10):
    for b in range(1, a+1):
        print("%dx%d=%d\t" % (a, b, a*b), end="")
    print("")