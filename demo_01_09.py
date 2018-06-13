#!usr/bin/python
# -*- coding:utf-8 -*-
'''
此文件环境使用python3 特例
大写的牛逼 佩服该作者 无报错 思路清晰
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urllib import request
from urllib.error import HTTPError
from taobao.tool import Tool
import re, os, threading

BASE_URL = 'http://mm.taobao.com/json/request_top_list.htm'
PATH = './MM/'


class Spider:
    def __init__(self, start_page, end_page):
        '''
        初始化
        :param start_page: 开始页面
        :param end_page: 结束页面
        '''
        self.base_url = BASE_URL
        self.start_page = start_page
        self.end_page = end_page
        self.client = webdriver.PhantomJS()
        self.tool = Tool()
        self.path = PATH

    def get_index_page(self, page):
        '''
        得到初始页面
        :param page: 传入参数是页面
        :return: 返回的是解码过后的页面
        '''
        url = self.base_url + '?page=' + str(page)
        req = request.Request(url)
        resp = request.urlopen(req)
        return resp.read().decode('gbk')

    def get_index_content(self, page):
        '''
        得到个人信息
        :param page: 页面
        :return: 携带个人5个信息的列表
        '''
        page_html = self.get_index_page(page)
        pattern = re.compile(
            '<a.*?class="lady-avatar">.*?<img src="(.*?)".*?<a class="lady-name" href="(.*?)" target="_blank">(.*?)</a>.*?<em><strong>(.*?)</strong>.*?<span>(.*?)</span>.*?<em>(.*?)</em>',
            re.S)
        items = re.findall(pattern, page_html)
        contents = []
        for item in items:
            mm_page_url = 'https:' + item[1]
            avatar_url = 'https:' + item[0]
            #[0] 头像的链接 [1] 个人详细信息的链接 [2] 名字 [3] 年龄 [4] 所在地 [5] 职业
            contents.append([avatar_url, mm_page_url, item[2], item[3], item[4], item[5]])
        return contents

    def get_infos_url(self, url):
        '''
        :param url: 个人详细信息的页面链接
        :return: 得到个人图片的域名地址
        '''
        self.client.get(url)
        try:
            element = self.client.find_element_by_class_name('mm-p-domain-info').find_element_by_tag_name('li')
            text = element.text
            return re.sub('域名地址', 'https', text)
        except NoSuchElementException as e:
            return None

    def get_infos_page(self, url):
        '''
        :param url: 个人图片的域名（原始网页上有（通过检查方式得到），网页源代码没有）
        :return: 页面的解码
        '''
        resp = request.urlopen(url)
        page_html = resp.read().decode('gbk')
        return page_html

    def get_infos_describe(self, page_html):
        '''
        得到个人经历
        :param page_html: 页面链接地址
        :return: 个人描述信息
        '''
        pattern = re.compile('<div class="mm-aixiu-content" id="J_ScaleImg">(.*?)<input', re.S)
        item = re.search(pattern, page_html)
        if not item:
            return None
        # remove duplicate urls
        desc = self.tool.replace(item.group(1))
        return desc

    def get_imgs_url(self, page_html):
        '''
        得到个人服装图片链接
        :param page_html: 解码页面
        :return: 图片链接列表
        '''
        pattern = re.compile('<img style=".*? src="(.*?)"')
        items = re.findall(pattern, page_html)
        urls = items[0:(len(items) // 2)]
        return urls

    def makedir(self, name):
        '''
        创建个人文件夹 用于存储信息
        :param name: 人名
        :return: 文件名
        '''
        dir_path = self.path + name + '/'
        exists = os.path.exists(dir_path)
        if not exists:
            print('create directory: %s' % dir_path)
            os.makedirs(dir_path)
        return dir_path

    def get_extension(self, img_url):
        '''
        :param img_url: 头像链接
        :return: 文件的类型
        '''
        return img_url.split('.')[-1]

    def save_img(self, img_url, file_path):
        '''
        :param img_url: 图片的链接
        :param file_path: 文件的存储位置
        :return: 无 打印文件存储的信息
        '''
        resp = request.urlopen(img_url)
        img = resp.read()
        with open(file_path, 'wb') as f:
            f.write(img)
        print('save img under: %s' % file_path)

    def save_info(self, content, file_path):
        '''
        存储个人的信息，名字 年龄 所在地 职业
        :param content: 个人信息的列表
        :param file_path: 文件位置
        :return: 无 打印存储信息
        '''
        info = 'name: %s\nage: %s\ncity: %s\ncareer: %s\n' % (content[2], content[3], content[4], content[5])
        with open(file_path, 'w') as f:
            f.write(info)
        print('save infos of %s at: %s' % (content[2], file_path))

    def save_describe(self, desc, file_path):
        '''
        保存个人描述信息
        :param desc: 个人
        :param file_path:
        :return:
        '''
        with open(file_path, 'w') as f:
            f.write(desc)
        print('save discribe at: %s' % file_path)

    def run(self):
        for i in range(self.start_page, self.end_page + 1):
            contents = self.get_index_content(i)
            for content in contents:
                dir_path = self.makedir(content[2])
                avatar_url = content[0]
                avatar_path = dir_path + content[2] + '.' + self.get_extension(content[0])
                self.save_img(avatar_url, avatar_path)
                info_path = dir_path + content[2] + 'infos.txt'
                self.save_info(content, info_path)
                url = self.get_infos_url(content[1])
                if not url:
                    print('domain not found')
                    continue
                print('domain: ' + url)
                page_html = self.get_infos_page(url)
                desc = self.get_infos_describe(page_html)
                if desc:
                    desc_path = dir_path + content[2] + 'description.txt'
                    self.save_describe(desc, desc_path)
                else:
                    print('No Description')
                img_urls = self.get_imgs_url(page_html)
                if img_urls:
                    imgs_path = dir_path + 'imgs/'
                    if not os.path.exists(imgs_path):
                        os.makedirs(imgs_path)
                    count = 1
                    for img_url in img_urls:
                        img_path = imgs_path + str(count) + '.' + self.get_extension(img_url)
                        img_url = 'https:' + img_url
                        try:
                            self.save_img(img_url, img_path)
                            count += 1
                        except HTTPError as e:
                            print(e.code)
                            print(e.msg)


spider1 = Spider(1, 1)
spider2 = Spider(2, 2)
t1 = threading.Thread(target=spider1.run)
t2 = threading.Thread(target=spider2.run)
t1.start()
t2.start()
t1.join()
t2.join()
print('Completed')
