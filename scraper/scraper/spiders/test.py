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

        hrefs_xpath = "//a/@href[contains(., 'facebook') or contains(.,'contact') or contains(.,'instagram') or contains(.,'twitter')]"
        #we are on the main website
        #Thats supposed to give us links for socials fb, ig, twitter and a contact page
        hrefs = response.xpath(hrefs_xpath).extract()
        print("links are here",hrefs)
        link="link"

        for href in hrefs:#we are going through links on the page to find socials
            #['http://smithgill.com/contact', 'https://www.twitter.com/smithgillarch',
            # 'https://www.facebook.com/smithgillarch', 'http://smithgill.com/contact',
            # 'https://www.twitter.com/smithgillarch', 'https://www.facebook.com/smithgillarch']
            print("the link is ",href)
            try:
                if "twitter" in href:
                    twitter_link = href
                    print("twitter link", twitter_link)
                    yield scrapy.Request(url=twitter_link, callback=self.parse_item,
                                         meta={'link': link, 'twitter': twitter_link,
                                               })
                    test2 = response.meta['twitter_key']
                    print("twitter test", test2)
            except Exception as e:
                print(e)
            try:
                if "contact" in href:
                    contact_link = href
                    print("contact link", contact_link)

                    yield scrapy.Request(url=contact_link, callback=self.parse_item,
                                         meta={'link': link,
                                               'contact': contact_link})
                    test1 = response.meta['contact_key']
                    print("contact test",test1)

            except Exception as e:
                print(e)



        #yield scrapy.Request(url="http://smithgill.com/contact", callback=self.parse_item,meta={'link':link,'facebook': facebook_link,'contact':contact_link})


    def parse_item(self, response):
        link = response.meta['link']
        try:
            twitter_link = response.meta['twitter']
            print("parse item twitter link: ",twitter_link)
            if twitter_link:
                print("twitter link is", twitter_link)
                twitter_test = "twitter works"
                yield scrapy.Request(url='http://smithgill.com/', callback=self.parse,
                                     meta={'twitter_key': twitter_test})
        except Exception as e:
            print("problem with twitter",e)
        try:
            contact_link = response.meta['contact']
            print("parse item contact link",contact_link)
            if contact_link:
                print("contact link is", contact_link)
                contact_test = "contact works"
                yield scrapy.Request(url='http://smithgill.com/', callback=self.parse,
                                     meta={'contact_key': contact_test})
        except Exception as e:
            print("problem with contact", e)

        #print("t1",link,"t2",facebook_link)
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
        phone_number = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', response.text)
        set_phone_number = set(phone_number)
        phone_number=list(set_phone_number)






        # for item in phone_number:
        #     try:
        #         if len(str(item)) == 11 and item[0]=="1":
        #             print(" phone number ", item , len(str(item)))
        #     except:
        #         print("no phone number")
        # for email in emails:
        #     print("email ", email)


    # def parse_google_result(self,response):
    #     company_name =""
    #
    #     url = "https://www.google.com/search?q="+ company_name
    #     seo_ranking = response.css('div[iUh30 tjvcx] a::text').get()
    #     google_rating = response.css('div[class=Aq14fc] a::text').get()
    #     google_review_count = response.css('div[class=hqzQac] a::text').get()


    #def data_save(self,company_name, email, phone_number, google_rating, website):
