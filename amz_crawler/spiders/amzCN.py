# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse



class AmzcnSpider(scrapy.Spider):
    name = "amzCN"
    allowed_domains = ["amazon.cn"]
    start_urls = (
#        'http://www.amazon.cn/',
        #单品
        #'http://www.amazon.cn/dp/B00NUAKQGA/',
#搜索
        'https://www.amazon.cn/s/?field-keywords=%s'%(u'理工'),
    )

    def parse(self, response):
        pass

    def parseList(self, response):
        sel = Selector(response=response)
        items = sel.xpath('//div[@id="resultsCol"]//li/div[@class="s-item-container"]')
        for item in items:
            print item.xpath('div[@class="a-row a-spacing-mini"]/div/a/h2/text()').extract()[0]
        
    def parseItem(self, response):
        sel = Selector(response=response)
        title = sel.xpath('//h1[@id="title"]/span[@id="productTitle"]/text()').extract()
        image = sel.xpath('//div[@id="img-canvas"]/img/@src').extract()

        #print response.body
        if title:
            print title[0]
        if image:
            print image[0]
