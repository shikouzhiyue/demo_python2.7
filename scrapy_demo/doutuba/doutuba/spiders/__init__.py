# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from doutuba.items import DoutubaItem


class Doutu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/article/list/?page={}'.format(i) for i in range(1, 10)]

    def parse(self, response):
        for content in response.xpath('//*[@id="home"]/div/div[1]/a[1]'):
            items = DoutubaItem()
            print type(content)
