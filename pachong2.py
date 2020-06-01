#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: pachong2.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 27, 2020
# ---

import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
# 定义请求头的浏览器代理， 伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
r = requests.get(link, headers=headers)  # 请求网页
soup = BeautifulSoup(r.text, "html.parser")  # 使用BeautifulSoup解析
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)  # 打印网页内容代码
# 打开一个空白Txt,然后写入刚刚获取的字符串title
with open('title_text.txt', 'a+') as f:
    f.write(title)
