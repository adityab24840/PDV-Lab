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