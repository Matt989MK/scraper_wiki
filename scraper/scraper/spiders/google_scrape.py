import scrapy
import logging
import urllib
import pandas as pd
import csv
import traceback
import re
import sys
class firstSpider(scrapy.Spider):
    name = 'companies'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_companies_in_the_Chicago_metropolitan_area']
    list_vars = []
    boom = []
    def __init__(self):
        self.big_chunky_list = []
        self._i = 0
        self.s_counter = 0
    counter = 0
    counter_x=0
    def parse(self, response):
        items = response.css('div[class=div-col] a::attr(href)').getall()
        for i, item in enumerate(items[:]):
            if "https://en.wikipedia.org" not in item:
                item = "https://en.wikipedia.org" + item
                link = response.urljoin(item)
            print(i)
            self.i = i
            try:
                yield scrapy.Request(url=link, callback=self.parse_businesses,
                                     meta={"max_retry_times": 2, "download_timeout": 20},
                                     errback=(lambda e: print("errback:", e)))
            except Exception as e:
                print(traceback.format_exc())


    def parse_businesses(self,response):
        try:
            page_link = response.css('span[class=url] a::attr(href)').get()
            link = response.urljoin(page_link)
            meta = {"link": link, "max_retry_times": 1, "download_timeout": 20}
            print(link,firstSpider.counter_x)
            firstSpider.counter_x+=1
            yield scrapy.Request(url=link, callback=self.parse_business, meta=meta,
                                 errback=(lambda e: print("errback:", e)))
        except Exception as e:
            print(e)



    def parse_business(self,response):
        #print("parse business")
        hrefs_xpath = "//a/@href[contains(., 'facebook') or contains(.,'contact') or contains(.,'instagram') or contains(.,'twitter')]"
        hrefs = response.xpath(hrefs_xpath).extract()
        #print("hrefs",hrefs)
        facebook_link=""
        twitter_link=""
        instagram_link=""
        contact_link=""
        emails =""
        phones=""
        link=response.meta.get("link").replace("http://","https://")
        firstSpider.counter+=1
        #firstSpider.boom=[]
        #print("parse business link: ",link)
        print("parse business", link, firstSpider.counter)

        for href in hrefs:
            try:
                if "facebook" in href:
                    facebook_link=href
                    #check ads + recent posts engagement ratio + posts on ads engagement ratio
                if "instagram" in href:
                    #check ads + recent posts engagement ratio + posts on ads engagement ratio

                    instagram_link=href
                if "twitter" in href:
                    #idk what yet
                    twitter_link=href
                try:
                    if "contact" in href:
                        contact_link = href
                        # print("contact link", contact_link)
                        yield scrapy.Request(url=contact_link, callback=self.parse_website,
                                             meta={'contact': contact_link,'link':link})
                        #test1 = response.meta['contact_key']
                        phones =response.meta['phones']
                        emails=response.meta['emails']
                        print("contact test_phones", phones,"emails",emails)
                        print(firstSpider.boom)
                except Exception as e:
                    print("error with yield is:",e)

            except Exception as e:
                print(traceback.format_exc())


        #
        try:
            print("link ", link, "facebook", facebook_link, " twitter ", twitter_link, " contact ", contact_link,
                  "email")
            self._i += 1
            print(self._i, '/', self.i)
            self.add_business(self.big_chunky_list,
                              urllib.parse.unquote(link, encoding='utf-8', errors='replace'), facebook_link,
                              instagram_link,
                              twitter_link, contact_link, emails, phones)
            # self.s_counter += 1
            #
            # if self.s_counter >= 20 or self._i == self.i:
            #     self.s_counter = 0
            #     self.dump_to_file()
            #     #sys.exit('listofitems not long enough')
            #     print('saved chunk')

        except Exception as e:
            print(traceback.format_exc())
            #emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
            #phone_number = re.findall(
             #   r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))',
             #   response.text)
       # self.add_business(self.big_chunky_list,
      #                    urllib.parse.unquote(link, encoding='utf-8', errors='replace'), facebook_link, instagram_link,
       #                   twitter_link, contact_link,emails,phone_number)
        #print(self.big_chunky_list)
        # try:
        #     #print("link ", link, "facebook",facebook_link," twitter ", twitter_link, " contact ", contact_link, "email")
        #     yield scrapy.Request(url=link, callback=self.parse_website, meta={'link':link,'facebook': facebook_link,'instagram':instagram_link,'twitter':twitter_link,'contact':contact_link})
        # except Exception as e:
        #     print(e)

    def parse_website(self,response):
        firstSpider.counter_x+=1
        link=response.meta['link']
        print("parse website", link, firstSpider.counter_x)
        #facebook_link=response.meta['facebook']
        #instagram_link=response.meta['instagram']
        #twitter_link=response.meta['twitter']
        #contact_link=response.meta['contact']
        test_var_contact = "contact Doesnt work"
        try:
            tt2 = response.meta['contact']
            if tt2:

                print("contact key")
                emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
                set_emails = set(emails)
                emails=list(set_emails)
                phone_number = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', response.text)

                for item in list(emails):
                    if ".com" not in item:
                        emails.remove((item))

                for item in list(phone_number):
                    print("this is attempt for phone",item)
                    try:
                        if len(str(item)) != 11 or item[0]!="1":
                            print("attempt succesful")
                            phone_number.remove(item)
                    except:
                        print("cant remove item")
                set_phone_number = set(phone_number)
                phone_number=list(set_phone_number)

                meta_contact = {'phones': phone_number, 'emails': emails}
                yield scrapy.Request(url=link, callback=self.parse,
                                     meta={'phones': phone_number, 'emails': emails})
                print("first spider test",firstSpider.boom,"meta_contact",meta_contact)
        except:
            print("unlucky")




        #print("email",emails,"phone",phone_number)
        # self.add_business(self.big_chunky_list,
        #                 urllib.parse.unquote(link, encoding='utf-8', errors='replace'), facebook_link, instagram_link,
        #                   twitter_link, contact_link,emails,phone_number)
        # # try:
        #     print(" phone number ", phone_number)
        # except:
        #     print("no phone number")
        # for email in emails:
        #     print("email ", email)
        #     yield {
        #         'URL': response.url,
        #         'Email': email
        #     }

    def dump_to_file(self):

        # for item in self.big_chunky_list:
        #     print("big chunky list ",item)
        print("This is dump to file")
        #print([[x.link,x.facebook_link, x.instagram_link, x.twitter_link, x.contact_link] for x in self.big_chunky_list])
        options = {}
        options['strings_to_formulas'] = False
        options['strings_to_urls'] = False
        writer = pd.ExcelWriter("results.xlsx", engine='xlsxwriter', options=options)


        lst = [[x.link,x.facebook_link, x.instagram_link, x.twitter_link, x.contact_link, x.email,x.phone_number] for x in self.big_chunky_list]
        df = pd.DataFrame(lst)
        df.to_csv('my_file.csv', index=False, header=False)
        writer.save()
        writer.close()
    def add_business(self,list,website_link,facebook_link="",instagram_link="",twitter_link="",contact_link="", email="",phone_number=""):

        try:

            new_business = Business(website_link, facebook_link, instagram_link, twitter_link, contact_link,email, phone_number)
            list.append(new_business)

        except Exception as e:
            print(e)


    def closed(self, reason):
        self.dump_to_file()
        logging.info("All work done")

class Business:
    def __init__(self, link, facebook_link,instagram_link,twitter_link,contact_link,email,phone_number):
        self.__link = link
        self.__facebook_link = facebook_link
        self.__instagram_link = instagram_link
        self.__twitter_link = twitter_link
        self.__contact_link = contact_link
        self.__email = email
        self.__phone_number = phone_number
    @property
    def link(self):
        return self.__link

    @property
    def facebook_link(self):
        return self.__facebook_link

    @property
    def instagram_link(self):
        return self.__instagram_link

    @property
    def twitter_link(self):
        return self.__twitter_link

    @property
    def contact_link(self):
        return self.__contact_link
    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number
