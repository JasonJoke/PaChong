#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: FTPpachong.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 27, 2020
# ---

# !/usr/bin/python
# coding=utf-8
import os
from ftplib import FTP  # 引入ftp模块


class MyFtp:
    ftp = FTP()

    def __init__(self, host, port=21):
        self.ftp.connect(host, port)

    def login(self, username, pwd):
        self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username, pwd)
        print(self.ftp.welcome)

    def downloadFile(self, localpath, remotepath, filename):
        os.chdir(localpath)  # 切换工作路径到下载目录
        self.ftp.cwd(remotepath)  # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        file_handle = open(filename, "wb").write  # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename), file_handle, blocksize=1024)  # 下载ftp文件
        # ftp.delete（filename）  # 删除ftp服务器上的文件

    def close(self):
        self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()


if __name__ == '__main__':
    ftp = MyFtp('10.18.34.24')
    ftp.login('idcmftp', 'Hryt@123')
    ftp.downloadFile('C:\\Users\\ShileiWu\\PCimg',
                     '/idcm-release/dailybuild/gin-dev/2020-05-28-01-00-00/', 'build.log')
    ftp.close()
