#!/usr/bin/env python
#coding:utf-8

# 法1
# import os
# return1=os.system('ping 8.8.8.8 -c 2') 
# if return1:
    # print 'ping fail'
# else:
    # print 'ping ok'

# 法2
# import os
# import subprocess
 
# fnull = open(os.devnull, 'w')
# return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
# if return1:
	# print 'ping fail'
# else:
	# print 'ping ok'
# fnull.close()

import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://115.239.210.26',timeout=1)
        return True
    except urllib2.URLError as err: 
        pass
        return False
	
if internet_on():
	print '网络未中断'
else:
	print '网络已中断'	
	
