import pandas as pd
import scrapy
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlencode

#API = '18fa7b1832038d45d7c56aa19587272a'
API = 'e5d9f2d2-58ea-4e33-8f6e-ef9fbb67908d'
def get_url(url):
    payload = {'api_key': API, 'proxy': 'residential', 'timeout': '20000', 'url': url}
    proxy_url = 'https://api.webscraping.ai/html' + urlencode(payload)
    print(proxy_url)
    return proxy_url


class google_seo_scraper(scrapy.Spider):
    name = 'google_seo'
    #allowed_domains = ['api.webscraping.ai']
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 5}


    def start_requests(self):
        url = 'https://www.google.com/search?client=firefox-b-d&q=Stomatologia+Tamka+%E2%80%A2+Stomatologia+Solec+%E2%80%A2+Dentysta+Warszawa+%E2%80%A2+NFZ'
        print("new url",get_url(url))
        yield scrapy.Request(get_url(url), callback=self.parse, meta={'pos': 0})


    def parse(self, response):
        print("parse live")


        # df = pd.DataFrame()
        # xlink = LinkExtractor()
        # link_list = []
        # link_text = []
        # divs = response.xpath('//div')
        # text_list = []
        # for span in divs.xpath('text()'):
        #     if len(str(span.get())) > 100:
        #         text_list.append(span.get())
        # for link in xlink.extract_links(response):
        #     if len(str(link)) > 200 or 'Journal' in link.text:
        #         # print(len(str(link)),link.text,link,"\n")'''
        #         link_list.append(link)
        #         link_text.append(link.text)
        # for i in range(len(link_text) - len(text_list)):
        #     text_list.append(" ")
        # df['links'] = link_list
        # df['link_text'] = link_text
        # df['text_meta'] = text_list
        # df.to_csv('output.csv')



        seo_ranking =  response.css('.iUh30.tjvcx').get() #that returns 1st website, loop thru first page

        google_rating = response.css('.Aq14fc::text').get()
        google_review_count = response.css('.hqzQac span::text').get()
        phone_number =response.css('.LrzXr.zdqRlf.kno-fv span::text').get()
        address= response.css('.LrzXr::text').get()

        print("seo ranking ",seo_ranking, " google rating ", google_rating," google review count ", google_review_count, phone_number, address)



