# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ItjuziItem
import re


class JuziSpider(CrawlSpider):
    name = 'juzi'
    allowed_domains = ['itjuzi.com']

    # offset = 1
    # url = 'https://www.itjuzi.com/company?page='
    start_urls = ['https://www.itjuzi.com/company?page=1']

    rules = (
        # 跟进每一页
        Rule(LinkExtractor(allow=r'www.itjuzi.com/company?page=\d+')),
        # 抓取每一家公司
        Rule(LinkExtractor(allow=r'www.itjuzi.com/company/\d+'), callback='parse_item', follow=True),
    )

    # start_urls = ['https://www.itjuzi.com/company/83300']

    # 第一个url会执行这个函数 这个函数会覆盖其他回调函数
    # （或者使用start_request()　不会覆盖，建议使用，用来发送请求）
    # def parse(self,response):
    #     pass


    def parse_item(self, response):
        print '**************'
        item = ItjuziItem()

        # 公司名字也是一个列表，因为有可能有多个名字
        companyName = response.xpath('//h1[@class="seo-important-title"]/text()').extract()[0].replace('/','')
        item['companyName'] = re.findall('\S+',companyName)

        item['round'] = response.xpath('//h1[@class="seo-important-title"]/span/text()').extract()[0].strip()
        item['shortNote'] = response.xpath('//div[@class="info-line"]/h2/text()').extract()[0].strip()
        item['bigSort'] = response.xpath('//div[@class="info-line"]/span[1]/a[1]/text()').extract()[0].strip()

        try:
            item['smallSort'] = response.xpath('//div[@class="info-line"]/span[1]/a[2]/text()').extract()[0].strip()
        except:
            item['smallSort'] = ''

        try:
            item['bigCity'] = response.xpath('//div[@class="info-line"]/span[@class="loca c-gray-aset"]/a[1]/text()').extract()[0].strip()
        except:
            item['smallCity'] = ''

        try:
            item['compannySite'] = response.xpath('//div[@class="link-line"]/a[4]/@href').extract()[0].strip()
        except:
            item['compannySite'] = 'NULL'

        # tag抓取的是一个列表
        item['tag'] = response.xpath('//div[@class="rowfoot"]/div/a/span/text()').extract()

        # 有可能是一个或者两个元素
        item['detailNote'] = response.xpath('//div[@class="block"][2]/div/text()').extract()[-1].strip()

        moreInfo = response.xpath('//div[@class="des-more"]/div/h2/text()').extract()
        item['companyFullName'] = moreInfo[0].split(u'\uff1a')[1]
        item['buildTime'] = moreInfo[1].strip().split(u'\uff1a')[1]
        item['scale'] = moreInfo[2].strip().split(u'\uff1a')[1]


        self.printtest(item)

        yield item



    def printtest(self,item):
        print '<---------print大法好--------->'
        # print item['companyName']
        # print item['round']
        # print item['shortNote']
        # print item['bigSort']
        # print item['smallSort']
        # print item['bigCity']
        # print item['smallCity']
        # print item['compannySite']
        # print '****',item['tag']
        # print item['detailNote']
        print item['companyFullName']
        print item['buildTime']
        print item['scale']
        print '<---------------------------->'