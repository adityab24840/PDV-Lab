import scrapy
from amazon_single_page_search.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/Echo-Dot-4th-Gen-Blue/dp/B084KSRFXJ/ref=sr_1_1?crid=XT8SVAQ7A0NF&keywords=alexa&qid=1695968402&sprefix=ale%2Caps%2C242&sr=8-1']

    def parse(self, response):
        items = AmazonItem()

        product_blocks = response.css('.s-result-item')
        for product_block in product_blocks:
            name = product_block.css('.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product_block.css('.a-price .a-offscreen::text').get()
            brand = product_block.css('.a-size-base-plus.a-color-base::text').get()

            items['name'] = name.strip() if name else None
            items['price'] = price.strip() if price else None
            items['brand'] = brand.strip() if brand else None

            yield items
