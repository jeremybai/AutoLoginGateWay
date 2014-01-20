# -*- coding: utf-8 -*-
import urllib
import urllib2
import socket
import sys
import time
import ConfigParser
import os


class Login(object):
	def __init__(self):
		self.user = self.pwd = self.url = ' '
	def setinfo(self, user, pwd, url):
		self.user = user
		self.pwd = pwd
		self.url = url
	def login_in(self):	
		data = {
			'TextBox1' : self.user,  #用户名
			'TextBox2' : self.pwd,   #密码
			'nw' : 'RadioButton1',   #免费地址
			'tm' : 'RadioButton6',	 #登陆2个小时
			'Button1' : u'登录网关'.encode('gb2312'),
			'__VIEWSTATE' :'/wEPDwUKMTM2NjA4NzMwMw8WAh4IcGFzc3dvcmQFCjUwNjUxMjV6eGMWAgIBD2QWDAIBDxYCHgRUZXh0ZWQCAw8PFgIfAWVkZAIFDxYCHwFlZAIHDxYCHgdWaXNpYmxlZ2QCCQ8WAh8CaGQCCw8WAh8BBTDlvZPliY3lnKjnur/kurrmlbA6PGIgc3R5bGU9J2NvbG9yOnJlZCc+MjA5OTwvYj5kGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYIBQxSYWRpb0J1dHRvbjEFDFJhZGlvQnV0dG9uMgUMUmFkaW9CdXR0b24zBQxSYWRpb0J1dHRvbjQFDFJhZGlvQnV0dG9uNQUMUmFkaW9CdXR0b242BQxSYWRpb0J1dHRvbjcFDFJhZGlvQnV0dG9uOA==',
			'__EVENTVALIDATION':'/wEWDQLF1pCSCQLs0bLrBgLs0fbZDALazsi9CQLazrwZAtTO6PQIAtTO/K8HAtTOgIoOAtTOlOUGAtTOuMANAtTOzLwEAoznisYGAoXZ9dsD'
		   }
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
		headers = {'User-Agent' : user_agent }
		postdata = urllib.urlencode(data)
		# print postdata
		request = urllib2.Request(self.url, postdata, headers)
		response = urllib2.urlopen(request)
		the_page = response.read()
		
		
def internet_on():
    try:
        response=urllib2.urlopen('http://115.239.210.26',timeout=3) 
        return True
    except urllib2.URLError as e: 
        print u"urllib2.URLError错误" 
    except socket.error as e: 
		type, value, traceback = sys.exc_info()[:3] 
		if type == socket.timeout: 
			print u"socket.timeout错误" 
		else: 
			print u"其他socket错误"
    return False
 
if __name__=='__main__':
	try:
		# 获得配置文件中的信息
		config = ConfigParser.SafeConfigParser()
		# 读取配置文件
		config.read(os.path.dirname(os.path.abspath(__file__)) + '/UserInfo.ini')
		# sections = config.sections()
		# print sections
		# 获取配置文件中的字段
		user = config.get('Info','UserID')
		pwd = config.get('Info','PassWord')	
	except ConfigParser.NoSectionError as e:
		print u'Error：用户信息未配置，请将您的学号和密码填入UserInfo.ini文件'
		while True:
			pass
	url = 'http://wg.suda.edu.cn/indexn.aspx'
	while True:
		suda = Login()
		suda.setinfo(user, pwd, url)
		if internet_on():
			print time.strftime('INFO - [%Y-%m-%d--%H:%M:%S] - ',time.localtime(time.time())),
			print u'网络未中断'
		else:
			print time.strftime('INFO - [%Y-%m-%d--%H:%M:%S] - ',time.localtime(time.time())),			
			print u'网络已中断,正在登陆网关...'	   
			suda.login_in()
			print u'网关已登陆'
		time.sleep(1)