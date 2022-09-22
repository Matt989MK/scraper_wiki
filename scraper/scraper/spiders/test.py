import sys
import re
import scrapy
import pandas
from scrapy.linkextractors import LinkExtractor
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule

class firstSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://smithgill.com/']
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )
    def parse(self, response):
        print("call parse")

        hrefs_xpath = "//a/@href[contains(., 'facebook') or contains(.,'contact') or contains(.,'instagram') or contains(.,'twitter')]"


        # with scrapy, you extract this xpath pattern
        hrefs = response.xpath(hrefs_xpath).extract()
        print(hrefs)
        for href in hrefs:

            if "facebook" or "contact" in href:
                print("now going to URL: ", href)
                yield response.follow(href, self.parse_item)
            else:
                print("")

    def parse_item(self, response):

        emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
        phone_number = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', response.text)
        try:
            print(" phone number ", phone_number)
        except:
            print("no phone number")
        for email in emails:
            print("email ", email)
            yield {
                'URL':response.url,
                'Email': email
                }


    # def parse_google_result(self,response):
    #     company_name =""
    #
    #     url = "https://www.google.com/search?q="+ company_name
    #     seo_ranking = response.css('div[iUh30 tjvcx] a::text').get()
    #     google_rating = response.css('div[class=Aq14fc] a::text').get()
    #     google_review_count = response.css('div[class=hqzQac] a::text').get()


    #def data_save(self,company_name, email, phone_number, google_rating, website):
