# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ItjuziItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyName = Field()
    round = Field()
    shortNote = Field()
    bigSort = Field()
    smallSort = Field()
    bigCity = Field()
    smallCity = Field()
    compannySite = Field()
    tag = Field()
    detailNote = Field()
    companyFullName = Field()
    buildTime = Field()
    scale = Field()
    catchTime = Field()
    spidername = Field()
