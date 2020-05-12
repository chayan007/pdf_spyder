# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from pdf_scraper.constants import TARGET_URLS, Selectors, PDF_EXTENSION, STRIP_STRING, BASE_URI
from pdf_scraper.spiders.pdf_resource import PDFItem


class PrivacyGovSpider(scrapy.Spider):
    name = 'privacy_gov'
    allowed_domains = ['privacy.gov.ph']
    start_urls = TARGET_URLS

    def parse(self, response):
        for href in response.xpath(Selectors.HREF_XPATH):
            link = href.extract()
            if link.endswith(PDF_EXTENSION):
                if link.startswith(STRIP_STRING):
                    link = '{}/{}'.format(
                        BASE_URI,
                        link.split(STRIP_STRING)[-1]
                    )
                    item = PDFItem()
                    item['file_urls'] = [link]
                    # yield item
                    yield Request(url=link, callback=self.save_pdf)

    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
