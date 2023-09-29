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