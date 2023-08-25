# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:33:01 2023

@author: aditya
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ('http://quotes.toscrape.com/',)
    
    
    def parse(self, response):
        title = response.css('title::text').extract()  #output= string
        yield {'titletest': title}
        
        all_div_quotes = response.css('div.quote')
        quote_details = []
        items = {}
        for quote in all_div_quotes:
            quotes = quote.css('span.text::text').extract()
            authors = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            items['quotes'] = quotes
            items['authors'] = authors
            items['tags'] = tags
            quote_details.append(items)
        yield {'Quote_List':quote_details}
