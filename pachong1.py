#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: pachong1.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 26, 2020
# ---

from urllib import request

url = "http://www.baidu.com"
respons = request.urlopen(url, timeout=2)
print(respons.read().decode('utf-8'))
