import scrapy


class PDFItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field