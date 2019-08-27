# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据源、采集时间、企业名称、浏览次数、口号、公司性质、行业分类、企业简介、好评度、薪资、融资信息、地址信息、联系方式

    data_source = scrapy.Field()
    time_stamp = scrapy.Field()
    company_name = scrapy.Field()
    browse = scrapy.Field()
    slogan = scrapy.Field()
    industry = scrapy.Field()
    category = scrapy.Field()
    desc = scrapy.Field()
    praise = scrapy.Field()
    salary = scrapy.Field()
    financing = scrapy.Field()
    address = scrapy.Field()
    contact = scrapy.Field()
    pass
