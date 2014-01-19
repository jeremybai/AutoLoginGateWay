# -*- coding: utf-8 -*-
import os
import urllib2
import cookielib
from urllib2 import urlopen, Request

cookieFile = "cookies.dat"
testURL = 'http://www.renren.com'
# 为cookie jar 创建实例
cJar = cookielib.LWPCookieJar()
# 创建HTTPCookieProcessor的opener对象
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cJar))
# 安装HTTPCookieProcessor的opener
urllib2.install_opener(opener) 
# 创建一个Request对象
r = Request(testURL)
# 打开HTML文件
h = urlopen(r)
print u"1 页面的头部"
print h.info()
print u"2 页面是否重定向"
print h.geturl()
print u"3 页面的Cookies"
for ind, cookie in enumerate(cJar):
	print "%d - %s" % (ind, cookie)
#保存cookies
cJar.save(cookieFile)