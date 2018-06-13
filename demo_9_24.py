# -*-coding:utf-8-*-
import urllib2, urllib
import ssl
from json import loads
from train_station_names import station_names

ssl._create_default_https_context = ssl._create_unverified_context

city = {}
for i in station_names.split('@'):
    if not i:
        continue
    else:
        city[i.split('|')[1]] = i.split('|')[2]

train_date = '2017-10-11'
from_station = city['北京']
to_station = city['郑州']


def getList():
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(train_date, from_station, to_station)
    req = urllib2.Request(url)
    html = urllib2.urlopen(req).read()
    dict = loads(html)
    return dict['data']['result']

a=0
#23=软卧
#28=硬卧
#
for result in getList():
    a = result.split('|')
    if a[30] == u'无' or not a[30]:
        continue
    print u'有票，车次：%s' %a[3]

