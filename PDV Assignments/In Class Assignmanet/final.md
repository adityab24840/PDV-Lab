## Overview Summary

This report aims to provide a comprehensive guide to web scraping using Scrapy, a powerful and versatile web crawling and scraping framework. The report is divided into three main cases, each of which explores different aspects of web scraping and Scrapy implementation.

### Case 1: Single-Page Web Scraping

In this case, we demonstrate how to create a Scrapy project for single-page web scraping. We focus on extracting specific data, such as product titles and prices, from a single Amazon product page. The report includes step-by-step instructions, code explanations, and details on project structure, items, pipelines, and settings.

### Case 2: Multi-Page Web Scraping

Case 2 expands on the previous case by illustrating how to scrape data from multiple pages of search results on Amazon. We address challenges such as pagination and dynamic URL changes. The report provides a detailed walkthrough of code modifications and adjustments to handle multiple pages effectively.

### Case 3: Iterating Over Multiple Searches

The final case introduces a more advanced scenario where we iterate over multiple search queries and collect data from multiple Amazon search result pages. We explore the concept of iterating over different queries, each with its own set of search results. The report includes code explanations and strategies for handling dynamic URL parameters.


---

**Report: Case 1 - Single Page Web Scraping**

**Objective:** To scrape data from a single web page on Amazon, specifically extracting product titles and prices.

**Project Structure:**

- **Items Code (items.py):**

  ```python
  import scrapy

  class AmazonItem(scrapy.Item):
      title = scrapy.Field()
      price = scrapy.Field()
  ```

  - Explanation: In the `items.py` file, we define a custom item class called `AmazonItem` with two fields: "title" and "price." These fields will be used to store the scraped data.

- **Pipeline Code (pipelines.py):**

  ```python
  class AmazonPipeline:
      def process_item(self, item, spider):
          # Perform data processing or validation here, if needed
          return item
  ```

  - Explanation: The `pipelines.py` file contains a custom pipeline class called `AmazonPipeline`. The `process_item` method is used to process each scraped item. You can implement data processing or validation logic inside this method.

- **Settings Code (settings.py):**

  ```python
  BOT_NAME = 'amazon_scraper'
  FEED_EXPORT_ENCODING = 'utf-8'
  NEWSPIDER_MODULE = 'amazon_scraper.spiders'
  ROBOTSTXT_OBEY = True
  SPIDER_MODULES = ['amazon_scraper.spiders']

  # Configure pipeline
  ITEM_PIPELINES = {
      'amazon_scraper.pipelines.AmazonPipeline': 300,
  }
  ```

  - Explanation: In the `settings.py` file, we configure project settings. These settings include the bot name, encoding for exported data, module for new spiders, whether to obey `robots.txt`, and the spider modules. We also configure the item pipeline to process items.

- **Spider Code (amazon_spider.py):**

  ```python
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
  ```

  - Explanation: The `amazon_spider.py` file contains the `AmazonSpider` class, which is responsible for web scraping. In the `parse` method, we use CSS selectors to extract the product title and price from the specified URL. We store the data in an `AmazonItem` object and yield it to pass it through the configured pipeline.

**Conclusion:**

In Case 1, we successfully created a Scrapy project for single-page web scraping from Amazon. We defined the item structure, set up a pipeline for data processing, and configured project settings accordingly. The spider was implemented to extract product titles and prices from the provided URL.

This project structure provides a foundation for more complex web scraping tasks, with the flexibility to customize data extraction and processing as needed.

---

**Report: Case 2 - Single Page Search Results Web Scraping**

**Objective:** To scrape data from a single page of search results on Amazon, specifically extracting product titles and prices for Manchester United jerseys.

**Project Structure:**

- **Items Code (items.py):**

  ```python
  import scrapy

  class AmazonItem(scrapy.Item):
      title = scrapy.Field()
      price = scrapy.Field()
  ```

  - Explanation: In the `items.py` file, we define a custom item class called `AmazonItem` with two fields: "title" and "price." These fields will be used to store the scraped data.

- **Pipeline Code (pipelines.py):**

  ```python
  class AmazonPipeline:
      def process_item(self, item, spider):
          # Perform data processing or validation here, if needed
          return item
  ```

  - Explanation: The `pipelines.py` file contains a custom pipeline class called `AmazonPipeline`. The `process_item` method is used to process each scraped item. You can implement data processing or validation logic inside this method.

- **Settings Code (settings.py):**

  ```python
  BOT_NAME = 'amazon_scraper'
  FEED_EXPORT_ENCODING = 'utf-8'
  NEWSPIDER_MODULE = 'amazon_scraper.spiders'
  ROBOTSTXT_OBEY = True
  SPIDER_MODULES = ['amazon_scraper.spiders']

  # Configure pipeline
  ITEM_PIPELINES = {
      'amazon_scraper.pipelines.AmazonPipeline': 300,
  }
  ```

  - Explanation: In the `settings.py` file, we configure project settings. These settings include the bot name, encoding for exported data, module for new spiders, whether to obey `robots.txt`, and the spider modules. We also configure the item pipeline to process items.

- **Spider Code (amazon_search_spider.py):**

  ```python
  import scrapy
  from amazon_scraper.items import AmazonItem

  class AmazonSearchSpider(scrapy.Spider):
      name = 'amazon_search_spider'
      start_urls = ['https://www.amazon.in/s?k=manchester+united+jersey']

      def parse(self, response):
          products = response.css('div.s-main-slot > div')
          
          for product in products:
              title = product.css('span.a-size-base-plus a-color-base a-text-normal::text').get()
              price = product.css('span.a-price span.a-offscreen::text').get()

              item = AmazonItem()
              item['title'] = title.strip() if title else None
              item['price'] = price.strip() if price else None

              yield item
  ```

  - Explanation: The `amazon_search_spider.py` file contains the `AmazonSearchSpider` class, responsible for web scraping. In the `parse` method, we use CSS selectors to extract product titles and prices from the search results page. We iterate through each product and store the data in an `AmazonItem` object before yielding it to pass it through the configured pipeline.

**Conclusion:**

In Case 2, we successfully created a Scrapy project for single-page web scraping from Amazon search results. We defined the item structure, set up a pipeline for data processing, and configured project settings accordingly. The spider was implemented to extract product titles and prices from the search results page for Manchester United jerseys.

This project structure provides a foundation for more complex web scraping tasks, with the flexibility to customize data extraction and processing as needed.

---

**Report: Case 3 - Multiple Page Search Results Web Scraping**

**Objective:** To scrape data from multiple pages of search results on Amazon, specifically extracting product titles and prices for Manchester United jerseys.

**Project Structure:**

- **Items Code (items.py):**

  ```python
  import scrapy

  class AmazonItem(scrapy.Item):
      title = scrapy.Field()
      price = scrapy.Field()
  ```

  - Explanation: In the `items.py` file, we define a custom item class called `AmazonItem` with two fields: "title" and "price." These fields will be used to store the scraped data.

- **Pipeline Code (pipelines.py):**

  ```python
  class AmazonPipeline:
      def process_item(self, item, spider):
          # Perform data processing or validation here, if needed
          return item
  ```

  - Explanation: The `pipelines.py` file contains a custom pipeline class called `AmazonPipeline`. The `process_item` method is used to process each scraped item. You can implement data processing or validation logic inside this method.

- **Settings Code (settings.py):**

  ```python
  BOT_NAME = 'amazon_scraper'
  FEED_EXPORT_ENCODING = 'utf-8'
  NEWSPIDER_MODULE = 'amazon_scraper.spiders'
  ROBOTSTXT_OBEY = True
  SPIDER_MODULES = ['amazon_scraper.spiders']

  # Configure pipeline
  ITEM_PIPELINES = {
      'amazon_scraper.pipelines.AmazonPipeline': 300,
  }
  ```

  - Explanation: In the `settings.py` file, we configure project settings. These settings include the bot name, encoding for exported data, module for new spiders, whether to obey `robots.txt`, and the spider modules. We also configure the item pipeline to process items.

- **Spider Code (amazon_multiple_pages_spider.py):**

  ```python
  import scrapy
  from amazon_scraper.items import AmazonItem

  class AmazonMultiplePagesSpider(scrapy.Spider):
      name = 'amazon_multiple_pages_spider'
      start_page = 1
      end_page = 7  # Number of pages to scrape
      base_url = 'https://www.amazon.in/s?k=manchester+united+jersey&page={page}&ref=sr_pg_{page}'

      def start_requests(self):
          for page in range(self.start_page, self.end_page + 1):
              url = self.base_url.format(page=page)
              yield scrapy.Request(url, callback=self.parse)

      def parse(self, response):
          products = response.css('div.s-main-slot > div')
          
          for product in products:
              title = product.css('span.a-size-base-plus a-color-base a-text-normal::text').get()
              price = product.css('span.a-price span.a-offscreen::text').get()

              item = AmazonItem()
              item['title'] = title.strip() if title else None
              item['price'] = price.strip() if price else None

              yield item
  ```

  - Explanation: The `amazon_multiple_pages_spider.py` file contains the `AmazonMultiplePagesSpider` class, responsible for web scraping. In the `start_requests` method, we generate multiple page URLs and send requests for each page. In the `parse` method, we extract product titles and prices from each page of search results. The spider is designed to scrape a specified range of pages, in this case, from page 1 to 7.

**Conclusion:**

In Case 3, we successfully created a Scrapy project for multiple-page web scraping from Amazon search results. We defined the item structure, set up a pipeline for data processing, and configured project settings accordingly. The spider was implemented to extract product titles and prices from a range of search results pages for Manchester United jerseys.

This project structure allows for efficient scraping of data from multiple pages and can be adapted for various web scraping scenarios.

---

## How to Contact Me

If you have any questions, need further assistance, or would like to get in touch with me, please feel free to reach out through the following contact methods:

### Email:

You can email me at [adityab24840@gmail.com](mailto:adityab24840@gmail.com) for any inquiries or assistance related to the report or the provided Scrapy projects.

### LinkedIn:

You can connect with me on LinkedIn at [Aditya N Bhatt](https://www.linkedin.com/in/adityabhatt015/) for professional networking and discussions.

### GitHub:

To access the Scrapy project codes and other technical resources, you can visit my GitHub repository at [adityab24840](https://github.com/adityab24840).

I am always happy to assist you and answer any questions you may have. Your feedback and inquiries are highly valued.

---
