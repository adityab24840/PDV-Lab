import scrapy

class RelianceDigitalProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()

