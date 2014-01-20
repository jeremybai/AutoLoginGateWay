## 自动登录苏州大学网关脚本
使用前将当前目录下的配置文件UserInfo.ini打开(编辑UserInfo.ini时不要使用微软的记事本，因为它在保存的时候会加上BOM头，最好使用notepad++编辑完选择格式为UTF-8无BOM格式编码然后保存。否则程序无法运行。)，将你的网关账号和密码填写到对应的UserID和PassWord，如：

    #网关账号和密码
    UserID = 2012XXXXXXX
    PassWord = XXXXXX

编辑好后保存关闭。
接下来运行AutoLoginGateWay.py或者双击AutoLoginGateWay.exe运行即可,程序在[这里](http://kuai.xunlei.com/d/ZmWaDoz8Ph3dUgQAef4)。
### 警告： ###
*1 请在使用前确保你的网关账号和密码正确。*   
*2 一直运行该程序可能会造成你的上网时间不够用，请先包月再使用。*  
*3 若不需要一直联网，则关闭该程序即可。*  
*4 这个程序对容错并没有做太多的考虑，只是实现了检测网络连接和登陆网关的功能。*
