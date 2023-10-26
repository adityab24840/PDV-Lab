import scrapy
from reliance_digital_scraper.items import RelianceDigitalProductItem

class RelianceDigitalSpider(scrapy.Spider):
    name = 'reliance_digital'
    start_urls = ['https://www.reliancedigital.in/page/redmi-mobiles']

    def parse(self, response):
        products = response.css('div.sp__product')
        for product in products:
            item = RelianceDigitalProductItem()
            item['title'] = product.css('p.sp__name::text').get()
            item['price'] = product.css('span.TextWeb__Text-sc-1cyx778-0.gimCrs span::text').get()
            yield item
