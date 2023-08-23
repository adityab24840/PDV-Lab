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
        #title = response.css('title').extract() #output=tage + string
        title = response.css('title::text').extract()  #output= string
        yield {'titletest': title}  