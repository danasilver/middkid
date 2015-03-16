# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MiddKidItem(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    professor = scrapy.Field()
    review_count = scrapy.Field()
    url = scrapy.Field()
