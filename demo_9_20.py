# -*- coding:utf-8 -*-
'''爬取京东的手机信息
特点 网页比较难找
输出存在问题 '''
import time
import sys
import requests
from lxml import etree
import json


def get_response(url):
    html = requests.get(url, headers=headers, timeout=5)
    selector = etree.HTML(html.text)
    product_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    sum = 0
    for product in product_list:
        try:
            sku_id = product.xpath('@data-sku')[0]
            product_url = 'http://item.jd.com/{}.html'.format(str(sku_id))
        except Exception as e:
            print e
    print sum


def get_data(product_url):
    product_dict = {}
    items = []
    html = requests.get(product_url, headers=headers)
    selector = etree.HTML(html.text)
    product_infos = selector.xpath('//ul[@class="parameter2 p-parameter-list"]')
    for product in product_infos:
        product_number = product.xpath('li[2]/@title')[0]
        product_price = get_product_price(product_number)
        product_dict['商品名称'] = product.xpath('li[1]/@title')[0]
        product_dict['商品id'] = product_number
        product_dict['商品产地'] = product.xpath('li[4]/@title')[0]
        product_dict['商品价格'] = product_price
        items.append(product_dict)
    for item in items:
        for i in item.values():
            print i


def get_product_price(sku):
    price_url = 'https://p.3.cn/prices/mgets?&skuIds=J_{}'.format(str(sku))
    response = requests.get(price_url, headers=headers).content
    response_json = json.loads(response)
    for info in response_json:
        return info.get('p')


if __name__ == '__main__':
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&cid2=653&cid3=655&page=1&s=64&click=0']
    # start_time = time.time()
    get_response(urls[0])
    # end_time = time.time()
    # print u'用时{}秒'.format(end_time - start_time)
