# -*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText
from user_agent import userAgent
import urllib, requests
import re
import threading
import time
'''爬取百思不得姐上面的视频并且下载，并且加上了本地的GUI'''
url_name = []
a = 1


def getUrl():
    global a
    url = 'http://www.budejie.com/video/' + str(a)
    headers = {'User-Agent': userAgent()}
    varl.set(r'已经获取到%s页的视频' %(a))
    html = requests.get(url, headers=headers).text
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)
    url_contents = re.findall(url_content, html)
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'
        url_regs = re.findall(url_reg, i)
        if url_regs:
            name_reg = re.compile(r' <a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            name_regs = re.findall(name_reg, i)
            for i, k in zip(name_regs, url_regs):
                url_name.append([i, k])
    return url_name


id = 1


def write():
    global id
    while id < 10:
        url_name = getUrl()
        for i in url_name:
            urllib.urlretrieve(i[1], 'video\\%s.mp4' % (i[0].encode('gbk')))
            text.insert(END, str(id) + '.' + i[1] + '\n' + 'i[0]' + '\n')
            url_name.pop(0)
            id += 1
    varl.set('抓取完毕！')


def start():
    th = threading.Thread(target=write)
    th.start()


'''本地窗口式'''
root = Tk()  # 实例化一个变量
# 名字
root.title('一苇万顷')
text = ScrolledText(root, font=('微软雅黑', 12))
text.grid()  # 实现布局方法
# 按钮
button = Button(root, text='开始爬取', font=('微软雅黑', 12), command = start)
button.grid()  # 增加按钮
# 绑定一个变量
varl = StringVar()
label = Label(root, font=('微软雅黑', 12), fg='blue', textvariable=varl)
label.grid()
varl.set('已经准备好...')
root.mainloop()  # 创建窗口指令
