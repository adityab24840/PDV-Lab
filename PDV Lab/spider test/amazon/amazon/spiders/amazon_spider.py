import scrapy
from amazon_scraper.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/Adidas-Mens-Regular-T-Shirt-H13881_Red/dp/B09NYKPR58/ref=sr_1_6?keywords=manchester+united+jersey&sr=8-6']

    def parse(self, response):
        title = response.css('span#productTitle::text').get()
        price = response.css('span#priceblock_ourprice::text').get()

        item = AmazonItem()
        item['title'] = title.strip() if title else None
        item['price'] = price.strip() if price else None

        yield item