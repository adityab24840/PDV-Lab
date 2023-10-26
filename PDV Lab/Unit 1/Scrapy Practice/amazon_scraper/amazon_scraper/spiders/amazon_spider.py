import scrapy
from amazon_scraper.items import AmazonProductItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/dp/B0C96V66GV/ref=sspa_dk_detail_3?ie=UTF8&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&pd_rd_i=B0C96V66GV&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&th=1&psc=1']

    def parse(self, response):
        item = AmazonProductItem()
        item['title'] = response.css('span#productTitle::text').get().strip()
        item['price'] = response.css('span.a-price-whole::text').get()
        item['brand'] = response.css('a#bylineInfo::text').get()
        yield item
