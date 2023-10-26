import scrapy

class AmazonProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
