#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: 1.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 28, 2020
# ---

import datetime

today = datetime.datetime.now()

offset = datetime.timedelta(days=-1)

d = today.strftime("%Y-%m-%d")+"-/d*-/d*-/d*"
print(d)