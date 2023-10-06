import scrapy
from amazon_single_page_search.items import AmazonItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/Echo-Dot-4th-Gen-Blue/dp/B084KSRFXJ/ref=sr_1_1?crid=XT8SVAQ7A0NF&keywords=alexa&qid=1695968402&sprefix=ale%2Caps%2C242&sr=8-1']

    def parse(self, response):
        product_item = AmazonItem()

        # Extract product details
        product_item['name'] = response.css('a-size-large product-title-word-break.a-text-normal::text').get().strip()
        product_item['price'] = response.css('a-price-whole::text').get().strip()
        product_item['brand'] = response.css('a-link-normal::text').get().strip()

        # Follow the link to the product reviews page
        reviews_link = response.css('a#acrCustomerReviewLink::attr(href)').get()
        if reviews_link:
            yield response.follow(reviews_link, self.parse_reviews, meta={'product_item': product_item})

    def parse_reviews(self, response):
        product_item = response.meta['product_item']

        # Extract reviews and description (you may need to adjust selectors)
        product_item['reviews'] = response.css('span.review-text-content::text').getall()
        product_item['description'] = response.css('div#productDescription p::text').get().strip()

        yield product_item
