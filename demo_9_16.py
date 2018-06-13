# -*- coding:utf-8 -*-
'''爬取淘女郎照片
特点 异步加载
格式化
编码
格式转化
图片下载
'''
import urllib2
from user_agent import userAgent
import json
import re
import os.path

def getUrl():
    req = urllib2.Request('https://mm.taobao.com/tstar/search/'
                          'tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent', userAgent())
    html = urllib2.urlopen(req,
                           data='q&viewFlag=A&sortType=default&searchStyle=&searchRegion'
                                '=city%3A&searchFansNum=&currentPage=1&pageSize=100'
                           ).read().decode('gbk').encode('utf-8')
    datajson = json.loads(html)
    return datajson['data']['searchDOList']


def getInfo(userid):
    req = urllib2.Request('https://mm.taobao.com/self/aiShow.htm?userId=%s' % userid)
    req.add_header('user-agent', userAgent())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    print html


def getAlbum(userid):
    req = urllib2.Request('https://mm.taobao.com/self/album/open_album_list.'
                          'htm?_charset=utf-8&user_id%%20=%s' % userid)
    req.add_header('user-agent', userAgent())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    reg = r'class="mm-first" href="//(.*?)"'
    return re.findall(reg, html)[::2]

def getPhotos():

    req = urllib2.Request('https://mm.taobao.com/album/json/get_album_photo_list.htm?'
                          'user_id=176817195&album_id=10000962815&top_pic_id=0'
                          '&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F176817195'
                          '%2FTB1jFcMKFXXXXblXFXXXXXXXXXX_!!0-tstar.jpg'
                          '&page=1&_ksTS=1505553820686_154&callback=jsonp155')
    req.add_header('user-agent', userAgent())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    middlephoto = re.split(r'"picUrl":"', html)
    lastphoto =[]
    for i in middlephoto:
        if i.startswith(r'//'):
            one = re.split('jpg', i)[0]
            lastphoto.append(one)
    return lastphoto

def savePhotos():
    num = 1
    item =getPhotos()
    for i in item:
        itemurl = 'http:' + i + 'jpg'
        req = urllib2.Request(itemurl)
        req.add_header('user-agent', userAgent())
        numphoto = 'D:\\taobaophoto\\' + str(num) + '.jpg'
        if os.path.exists(numphoto):
            pass
        else:
            with open(numphoto, 'wb') as fp:
                img = urllib2.urlopen(req)
                fp.write(img.read())
                print str(num)+'ok'
        num = num + 1

savePhotos()
# for i in getUrl():
#     userid = i['userId']
#     #print userid
#     #getInfo(userid)
#     # for n in getAlbum(userid):
#     #     print n
#     #break

