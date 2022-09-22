import pandas as pd
import scrapy
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlencode

API = '18fa7b1832038d45d7c56aa19587272a'

def get_url(url):
    payload = {'api_key': API, 'proxy': 'residential', 'timeout': '20000', 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    print(proxy_url)
    return proxy_url


class google_seo_scraper(scrapy.Spider):
    name = 'google_seo'
    #allowed_domains = ['api.webscraping.ai']
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 5}


    def start_requests(self):
        url = 'https://www.google.com/search?q=Western%20Iowa%20Dental%20Group/'
        print("new url",get_url(url))
        yield scrapy.Request(get_url(url), callback=self.parse, meta={'pos': 0})


    def parse(self, response):
        print("parse live")
        test = response.css('span[class=MUFPAc] a::text').get()
        print(test)

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


        response.xpath("//div[@class='Ob2kfd']/span[@class='Ob2kfd']/text()").extract()
        seo_ranking = response.css('div[class=TbwUpd]// a::attr(href)').getall()
        google_rating = response.xpath("/div[@class='Ob2kfd']//span[@class='Aq14fc']/text()").extract()
        google_review_count = response.css('span[class=hqzQac] ::*/text()').getall()
        print("seo ranking ",seo_ranking, " google rating ", google_rating," google review count ", google_review_count)



