# -*- coding: utf-8 -*-
import urllib
import urllib2
import socket
import sys
import time

	
	
url = 'http://wg.suda.edu.cn/indexn.aspx'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
headers = {'User-Agent' : user_agent }
data = {'TextBox1' : '20124227025',  #用户名
        'TextBox2' : '5065125zxc',   #密码
        'nw' : 'RadioButton1',
        'tm' : 'RadioButton6',
        'Button1' : u'登录网关'.encode('gb2312'),
        '__VIEWSTATE' :'/wEPDwUKMTM2NjA4NzMwMw8WAh4IcGFzc3dvcmQFCjUwNjUxMjV6eGMWAgIBD2QWDAIBDxYCHgRUZXh0ZWQCAw8PFgIfAWVkZAIFDxYCHwFlZAIHDxYCHgdWaXNpYmxlZ2QCCQ8WAh8CaGQCCw8WAh8BBTDlvZPliY3lnKjnur/kurrmlbA6PGIgc3R5bGU9J2NvbG9yOnJlZCc+MjA5OTwvYj5kGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYIBQxSYWRpb0J1dHRvbjEFDFJhZGlvQnV0dG9uMgUMUmFkaW9CdXR0b24zBQxSYWRpb0J1dHRvbjQFDFJhZGlvQnV0dG9uNQUMUmFkaW9CdXR0b242BQxSYWRpb0J1dHRvbjcFDFJhZGlvQnV0dG9uOA==',
        '__EVENTVALIDATION':'/wEWDQLF1pCSCQLs0bLrBgLs0fbZDALazsi9CQLazrwZAtTO6PQIAtTO/K8HAtTOgIoOAtTOlOUGAtTOuMANAtTOzLwEAoznisYGAoXZ9dsD'
       }
	  

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
 

while True:
	time.sleep(1)
	if internet_on():
		print u'网络未中断'
	else:
		print u'网络已中断,正在登陆网关...'	   
		postdata = urllib.urlencode(data)
		# print postdata
		request = urllib2.Request(url, postdata, headers)
		response = urllib2.urlopen(request)
		the_page = response.read()
		print u'网关已登陆'
