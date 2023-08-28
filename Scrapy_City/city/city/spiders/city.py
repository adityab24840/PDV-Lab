import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class RankSpider(scrapy.Spider):
    name = 'rank'
    start_urls = ["https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"]

    def parse(self, response):
        open_in_browser(response)

        table = response.xpath('//table[contains(@class, "wikitable")]')[0]
        trs = table.xpath('.//tr')[1:]  

        for tr in trs:
            rank = tr.xpath('.//td[1]/text()').extract_first().strip()
            city = tr.xpath('.//td[2]//text()').extract_first().strip()
            state = tr.xpath('.//td[5]//text()').extract_first().strip()
            
            yield {
                'rank': rank,
                'city': city,
                'state': state
            }
