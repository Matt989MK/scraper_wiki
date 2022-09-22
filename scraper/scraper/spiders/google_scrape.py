import sys

import scrapy
import pandas
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class firstSpider(scrapy.Spider):
    name = 'companies'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_companies_in_the_Chicago_metropolitan_area']

    def parse(self, response):

        items =   response.css('div[class=div-col] a::attr(href)').getall()
        for item in items:
            if "https://en.wikipedia.org" not in item:
                item="https://en.wikipedia.org"+item
                link = response.urljoin(item)

            #print(item)
            yield scrapy.Request(url=link, callback=self.parse_businesses)

    def parse_businesses(self,response):
        #print("executed")
        try:
            page_link = response.css('span[class=url] a::attr(href)').get()
            print(page_link)
            link = response.urljoin(page_link)

            yield scrapy.Request(url=link, callback=self.parse_business)
        except:
            print("failed to get link")



    def parse_business(self,response):
        print("parse business")
        hrefs_xpath = "//a/@href[contains(., 'business') or contains(.,'brand')]"
        #print(hrefs_xpath)
        contact_info = response.xpath(hrefs_xpath).extract()
        print(contact_info)
       # print(website_link)

        #print("contact info",contact_info)
        yield scrapy.Request(url = contact_info, callback=self.parse_contact_page)

    def parse_contact_page(self,response):
        print("contact page welcome")