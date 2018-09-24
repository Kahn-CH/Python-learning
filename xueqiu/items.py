# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueqiuItem(scrapy.Item):
    symbol = scrapy.Field()  # 股票代码
    code = scrapy.Field()  # 代码
    name = scrapy.Field()  # 名称
    current = scrapy.Field()  # 当前价
    percent = scrapy.Field()  # 涨跌幅
    change = scrapy.Field()  # 涨跌额
    high = scrapy.Field()  # 当日最高幅度
    low = scrapy.Field()  # 当日最低幅度
    high52w = scrapy.Field()  # 52周股价最高幅度
    low52w = scrapy.Field()  # 52周股价最低幅度
    marketcapital = scrapy.Field()  # 市值
    amount = scrapy.Field()  # 成交额
    pettm = scrapy.Field()  # 市盈率
    volume = scrapy.Field()  # 成交量


