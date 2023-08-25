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
        title = response.css('title::text').extract_first()
        authors = response.css('.author::text').extract_first()
        tags = response.css('.tag::text').extract_first()

        yield {
            'title': title,
            'authors': authors,
            'tags': tags
        }
