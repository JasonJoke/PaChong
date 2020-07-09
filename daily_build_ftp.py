# coding=utf-8

"""
author: MiaZhang
Created on 2020/6/2 15:59
"""
import ftplib
import socket
import datetime
from ftplib import FTP, error_perm
import os
import gzip
import tarfile

import shutil


def ftpconnect(host, port, username, password):
    ftp = FTP()
    ftp.set_debuglevel(0)
    try:
        ftp.connect(host, port)
        ftp.login(username, password)
    except (socket.error, socket.gaierror):
        print("ERROR: cannot connect [{}:{}]".format(host, port))
        return None
    except error_perm:
        print("ERROR: user Authentication failed")
        return None
    except:
        print("ERROR: Unknow")
        return None
    return ftp


# 下载文件，remotepath下载前的ftp的目标地址，localpath下载后的文件存放的本地目录
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    with open(localpath, 'wb') as fp:
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)


# 上传文件
# def uploadfile(ftp, remotepath, localpath):
#     bufsize = 1024
#     with open(localpath, 'rb') as fp:
#         ftp.storbinary('STOR ' + remotepath, fp, bufsize)


# 文件解压，file_name文件存放路径及文件名，imgpath存放路径
def unzip(file_name, imgpath):
    # 获取文件的名称，去掉后缀名
    f_name = file_name.replace(".gz", "")
    # 开始解压gz文件
    g_file = gzip.GzipFile(file_name)
    # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()
    # 开始解压tar文件
    tar = tarfile.open(f_name, 'r')
    tar.extractall(path=imgpath)
    tar.close()


if __name__ == "__main__":
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    remote_path_0 = "/idcm-release/dailybuild/gin-dev/" + time + "-01-00-00/gin-userdebug-img.tar.gz"
    remote_path_1 = "/idcm-release/dailybuild/gin-dev/" + time + "-01-00-01/gin-userdebug-img.tar.gz"
    local_path = "./" + time + "/gin-userdebug-img.tar.gz"
    if os.path.exists(time):
        shutil.rmtree(time)
        os.makedirs(time)
    else:
        os.makedirs(time)
    ftp = ftpconnect("10.18.34.24", 21, "idcmftp", "Hryt@123")
    try:
        downloadfile(ftp, remote_path_1, local_path)
    except ftplib.error_perm:
        downloadfile(ftp, remote_path_0, local_path)
    ftp.quit()
    unzip(local_path, time)
    os.system('cd ' + time)
    # os.system('..\dailyBuild.bat')
    os.system('cd ..')
    for i in range(2, 5):
        rm_time = (datetime.datetime.now() + datetime.timedelta(days=-i)).strftime("%Y-%m-%d")
        if os.path.exists(rm_time):
            shutil.rmtree(rm_time)
