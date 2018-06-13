#!usr/bin/python
# -*- coding:utf8 -*-

import urllib
import random
import time

# import socket

# socket.setdefaulttimeout(3)

inf = open("ip.txt")  # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0, len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://ip.chinaz.com/getip.aspx"
# 将可用ip写入valid_ip.txt
i = 0
for proxy in proxys:
    try:
        time.sleep(3 + random.random() * 3)
        i = i + 1
        res = urllib.urlopen(url, proxies=proxy).read()
        valid_ip = proxy['http'][7:]
        print 'valid_ip: ' + valid_ip
        with open("valid_ip.txt", "a+") as ouf:
            ouf.write(valid_ip)

    except Exception, e:
        print proxy
        print e
        continue
    if 1 == 20:
        break
