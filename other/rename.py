#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
rootdir = "/Users/huangxiquan/huangxiquan/包/吉林银行/吉林银行20160331"                                   # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	for filename in filenames:                        #输出文件信息
		print (filename) #输出文件路径信息
		index = filename.find("-unsigned.apk_singed")
		newFileName = filename.replace('-unsigned.apk_singed',"")
		print (newFileName)
		os.rename(os.path.join(parent, filename), os.path.join(parent, newFileName))  
