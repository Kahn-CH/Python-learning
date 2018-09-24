# -*- coding: utf-8 -*-
import json

import scrapy

from xueqiu.items import XueqiuItem


class XueqiuSpiderSpider(scrapy.Spider):
    name = 'xueqiu_spider'
    allowed_domains = ['xueqiu.com']

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'aliyungf_tc=AQAAAJ+IBCzC3gEA+4yccwS9q8wgN6Mp; s=di1xcn3ytf; xq_a_token=9c75d6bfbd0112c72b385fd95305e36563da53fb; xq_r_token=9ad364aac7522791166c59720025e1f8f11bf9eb; u=271536468210093; device_id=0d15e1c8ed47aae9f4629a81d3fa8057; __utmc=1; __utmz=1.1536468211.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.1155171146.1536468211.1536468211.1536472732.2; __utmt=1; __utmb=1.3.10.1536472732',
            'Host': 'xueqiu.com',
            'Referer': 'https://xueqiu.com/hq',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
    }

    def start_requests(self):
        cookies = {
            'aliyungf_tc': 'AQAAAJ+IBCzC3gEA+4yccwS9q8wgN6Mp',
            's': 'di1xcn3ytf',
            'xq_a_token': '9c75d6bfbd0112c72b385fd95305e36563da53fb',
            'xq_r_token': '9ad364aac7522791166c59720025e1f8f11bf9eb',
            'u': '271536468210093',
            'device_id': '0d15e1c8ed47aae9f4629a81d3fa8057',
            '__utmc': '1',
            '__utmz': '1.1536468211.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '__utma': '1.1155171146.1536468211.1536468211.1536472732.2',
            '__utmt': '1',
            '__utmb': '1.3.10.1536472732',
        }
        for page in range(1, 63):
            url = 'https://xueqiu.com/stock/cata/stocklist.json?page={0}&size=90&order=desc&orderby=percent&type=11%2C12&_=1536472902500'.format(page)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True, cookies=cookies, meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [301, 302]
            })

    def parse(self, response):
        item = XueqiuItem()
        try:
            res = json.loads(response.text)
            stocks = res['stocks']
            for stock in stocks:
                item['symbol'] = stock['symbol']
                item['code'] = stock['code']
                item['name'] = stock['name']
                item['current'] = stock['current']
                item['percent'] = stock['percent']
                item['change'] = stock['change']
                item['high'] = stock['high']
                item['low'] = stock['low']
                item['high52w'] = stock['high52w']
                item['low52w'] = stock['low52w']
                item['marketcapital'] = stock['marketcapital']
                item['amount'] = stock['amount']
                item['pettm'] = stock['pettm']
                item['volume'] = stock['volume']
                yield item
        except Exception:
            print("当前解析失败!")
            yield None
