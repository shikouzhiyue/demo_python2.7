'''12306查票'''
import urllib2
import re
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2017-10-11&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'
url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2017-10-01&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'

req = urllib2.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
html = urllib2.urlopen(req).read()
result_1 = json.loads(html)
result_2 = result_1['data']['result']
for result in result_2:
    a = 0
    result_3 = result.split('|')
    for i in result_3:
        print a, i
        a = a + 1
    break
