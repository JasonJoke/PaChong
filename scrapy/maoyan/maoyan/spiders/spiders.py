# -*- coding: utf-8 -*-
import scrapy


class SpidersSpider(scrapy.Spider):
    name = 'spiders'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
