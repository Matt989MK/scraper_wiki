import sys
import re
import scrapy
import pandas
from scrapy.linkextractors import LinkExtractor
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule

class firstSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.dragcity.com/']
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )
    list_vars=[]
    boom = []
    def parse(self, response):

        hrefs_xpath = "//a/@href[contains(., 'facebook') or contains(.,'contact') or contains(.,'instagram') or contains(.,'twitter')]"
        #we are on the main website
        #Thats supposed to give us links for socials fb, ig, twitter and a contact page
        hrefs = response.xpath(hrefs_xpath).extract()
        link="link"
        hrefs_set = set(hrefs)
        hrefs=hrefs_set
        #print("links are here",hrefs)
        firstSpider.boom = []
        for href in hrefs:#we are going through links on the page to find socials
            #['http://smithgill.com/contact', 'https://www.twitter.com/smithgillarch',
            # 'https://www.facebook.com/smithgillarch', 'https://www.twitter.com/smithgillarch'
            print("the link is ",href)
            twitter_link=""
            contact_link=""
            facebook_link=""
            try:
                if "twitter" in href:
                    twitter_link = href
                    #print("twitter link", twitter_link)
                    yield scrapy.Request(url=twitter_link, callback=self.parse_item,
                                         meta={'twitter': twitter_link})
                    test2 = response.meta['twitter_key']

                    print("twitter test", test2)
            except Exception as e:
                print(e)
            try:
                if "contact" in href:
                    contact_link = href
                    #print("contact link", contact_link)
                    yield scrapy.Request(url=contact_link, callback=self.parse_item,
                                         meta={'contact': contact_link})
                    test1 = response.meta['contact_key']

                    print("contact test",test1)
            except Exception as e:
                print(e)
            try:
                if "facebook" in href:
                    facebook_link = href
                    # print("contact link", contact_link)
                    yield scrapy.Request(url=facebook_link, callback=self.parse_item,
                                         meta={'facebook': facebook_link})
                    test3 = response.meta['facebook_key']

                    print("facebook test", test3)
            except Exception as e:
                print(e)
            #variables overwrite themselves thats the problem. Make a list in the beginning and append. If containts dont replace

            print(firstSpider.boom)


        #yield scrapy.Request(url="http://smithgill.com/contact", callback=self.parse_item,meta={'link':link,'facebook': facebook_link,'contact':contact_link})



    def parse_item(self, response):
        #link = response.meta['link']
        # print("parse item link:",link)
        test_var = "twitter Doesnt work"
        test_var_contact ="contact Doesnt work"
        test_var_facebook="facebook Doesnt work"


        try:
            tt=response.meta['twitter']
            if tt:
                #print("twitter key")
                test_var=" twitter works"
                firstSpider.boom.append(test_var)
        except:
            print("unlucky")

        try:
            tt2 = response.meta['contact']
            if tt2:

                #print("contact key")
                emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
                set_emails = set(emails)
                emails=list(set_emails)
                phone_number = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', response.text)
                set_phone_number = set(phone_number)
                phone_number=list(set_phone_number)
                test_var_contact = " contact works"

                firstSpider.boom.append(phone_number)
                firstSpider.boom.append(emails)
        except:
            print("unlucky")
        try:
            tt3 = response.meta['facebook']
            if tt3:
                # print("contact key")
                test_var_facebook = "facebook works"
                firstSpider.boom.append(test_var_facebook)
        except:
            print("unlucky")

            #test_var_contact="modification contact"
        meta_twitter = {'contact_key': test_var_contact, 'twitter_key': test_var,'facebook_key':test_var_facebook}


        #firstSpider.boom.append({test_var_contact,test_var,test_var_facebook})
        print("list",firstSpider.boom)
        print("meta",meta_twitter)
        #print(meta_twitter)
        yield scrapy.Request(url='https://www.dragcity.com/', callback=self.parse,
                             meta=meta_twitter)
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
