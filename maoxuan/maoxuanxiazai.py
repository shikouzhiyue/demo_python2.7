#!usr/bin/python
# -*-coding:utf-8-*-
import urllib
import urllib2
import re
import random
from bs4 import BeautifulSoup
import time


class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


tool = Tool()
contents = []
user_agent_list = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
headers = {'User-Agent': random.choice(user_agent_list)}
url_3 = 'http://www.dudj.net/hongsejingdian/46/{}.html'
url_4 = 'http://www.dudj.net/hongsejingdian/50/{}.html'
for page in range(1109, 1141):
    request = urllib2.Request(url_3.format(page), headers=headers)
    response = urllib2.urlopen(request)
    Soup = BeautifulSoup(response.read(), 'lxml')
    title = Soup.find('h2').get_text()
    print u'开始 %s 的 下载' % title
    time.sleep(3 + random.random() * 3)
    content = Soup.find('div', class_='zw').find_all('p')
    with open(u'毛选第三卷' + '.txt', 'a+') as f:
        f.write('\n'+title.encode('utf-8')+'\n')
    for i in content:
        duanluo = "\n" + tool.replace(i.get_text()) + "\n"
        with open(u'毛选第三卷' + '.txt', 'a+') as f:
            f.write(duanluo.encode('utf-8'))
# for page in range(1141, 1174):
#     request = urllib2.Request(url_4.format(page), headers=headers)
#     response = urllib2.urlopen(request)
#     Soup = BeautifulSoup(response.read(), 'lxml')
#     title = Soup.find('h2').get_text()
#     print u'开始 %s 的 下载' % title
#     time.sleep(3 + random.random() * 3)
#     content = Soup.find('div', class_='zw').find_all('p')
#     with open(u'毛选第四卷' + '.txt', 'a+') as f:
#         f.write(title.encode('utf-8'))
#     for i in content:
#         duanluo = "\n" + tool.replace(i.get_text()) + "\n"
#         with open(u'毛选第四卷' + '.txt', 'a+') as f:
#             f.write(duanluo.encode('utf-8'))
# for page in range(1378, 1415):
#     request = urllib2.Request(url_4.format(page), headers=headers)
#     response = urllib2.urlopen(request)
#     Soup = BeautifulSoup(response.read(), 'lxml')
#     title = Soup.find('h2').get_text()
#     print u'开始 %s 的 下载' % title
#     time.sleep(3 + random.random() * 3)
#     content = Soup.find('div', class_='zw').find_all('p')
#     with open(u'毛选第四卷' + '.txt', 'a+') as f:
#         f.write(title.encode('utf-8'))
#     for i in content:
#         duanluo = "\n" + tool.replace(i.get_text()) + "\n"
#         with open(u'毛选第四卷' + '.txt', 'a+') as f:
#             f.write(duanluo.encode('utf-8'))

print u'完成'
