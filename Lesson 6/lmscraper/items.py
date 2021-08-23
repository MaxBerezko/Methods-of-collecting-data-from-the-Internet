# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class LmscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
