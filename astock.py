# -*- coding:utf8 -*- 

def parseRes(res):
	return res.split('\n')

def parseText(text):
	fs="\""
	fq=text.find(fs)
	lq=text.rfind(fs)
	vtext=text[fq+1:lq].strip()
	if len(vtext)>0:
		# print vtext
		arr=vtext.split(",")
		data={}
		data['name']=arr[0]
		data['openprice']=arr[1]
		data['yescloseprice']=arr[2]
		data['price']=arr[3]
		data['topprice']=arr[4]
		data['bottomprice']=arr[5]
		data['dealmoney']=arr[9]
		data['date']=arr[30]
		return data
	return None

def outPutDatalist(datas):
	for data in datas:
		yc = float(data['yescloseprice'])
		pri = float(data['price'])
		print "%s %1.2f%%" % (data['name'],(pri-yc)/yc*100)

import sys
if len(sys.argv)<=1:
	print "python astock.py [stockcode ...]"
	print "For example: python astock.py sh600320 sz000029"
	exit(1)

subpath = ",".join(sys.argv[1:])

import urllib
import time
import json
import os

BaseUrl = "http://hq.sinajs.cn/list="
datalist=[]
url = BaseUrl + subpath
f = urllib.urlopen(url)
res = f.read()
f.close()
res = res.decode('GB2312')
texts  = parseRes(res)
for text in texts:
	data = parseText(text)
	if data!=None:
		datalist.append(data)
outPutDatalist(datalist)
