# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import HTMLParser  # 实现HTML文件的分析
import sys
'''爬取知乎日报 并且通过解析得到文章内容'''

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取源码
def getHtml(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request, timeout=5)
    text = response.read()
    return text


# 获取链接
def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"')
    items = re.findall(pattern, html)
    urls = []
    for item in items:
        urls.append('http://daily.zhihu.com/story/' + item)
    return urls


# 获取内容
def getContent(url):
    print url
    html = getHtml(url)
    header_pattern = re.compile('<h1 class="headline-title">(.*?)</h1>', re.S)
    header_items = re.findall(header_pattern, html)
    print '-' * 10 + header_items[0] + '-' * 10
    content_pattern = re.compile(r'<hr />(.*?)<hr />', re.S)
    content_items = re.findall(content_pattern, html)
    # print content_items
    for content_item in content_items:
        for content in characterProcessing(content_item):
            print content

# 提取内容 然后进行 过滤，感觉在别的地方也可以用
def characterProcessing(html):
    htmlParser = HTMLParser.HTMLParser()
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?', re.S)
    items = re.findall(pattern, html)
    result = []
    for index in items:
        if index != '':
            for content in index:
                tag = re.search('<.*?>', content)
                http = re.search('<.*?gtto.*?', content)
                html_tag = re.search('&', content)
                if html_tag:
                    content = htmlParser.unescape(content)
                if http:
                    continue
                elif tag:
                    pattern = re.compile('(.*?)<.*?>(.*?)</.*?>(.*)')
                    items = re.findall(pattern, content)
                    content_tags = ''
                    if len(items) > 0:
                        for item in items:
                            if len(item) > 0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + item
                        content_tags = re.sub('<.*?>', '', content)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result


#
html = getHtml(url='http://daily.zhihu.com/')
# urls = getUrls(html)
# for u in urls:
#     getContent(u)
#     break
getContent(url='http://daily.zhihu.com/story/9621221')
