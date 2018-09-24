# -*- coding: utf-8 -*-
from scrapy.exporters import CsvItemExporter


class XueqiuPipeline(object):
    def open_spider(self, spider):
        self.file = open("./data.csv", "wb")
        self.exporter = CsvItemExporter(self.file,
        fields_to_export=["symbol", "code", "name", 'current', 'percent', 'change', 'high', 'low', 'high52w', 'low52w', 'marketcapital', 'amount', 'pettm', 'volume'])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
