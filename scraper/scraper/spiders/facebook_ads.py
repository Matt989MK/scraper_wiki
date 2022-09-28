import scrapy
from urllib.parse import urlencode

API = '18fa7b1832038d45d7c56aa19587272a'

def get_url(url):
    payload = {'api_key': API, 'proxy': 'residential', 'timeout': '20000', 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    #print(proxy_url)
    return proxy_url


class google_seo_scraper(scrapy.Spider):
    name = 'facebook_ads'
    #allowed_domains = ['api.webscraping.ai']
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 5}

    def start_requests(self):
        url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=20825389113&search_type=page&media_type=all'
        print("new url", get_url(url))
        print('normal url', url)
        yield scrapy.Request(url, callback=self.parse, meta={'pos': 0})



    def parse(self, response):
        print("parse live2")


        ads_list = response.css('.hael596l.alzwoclg.o7bt71qk.srn514ro.k70v3m9n.rl78xhln.dwuburet.n6l8ih64.e7mudugv.nra9ig5p.atzpf96a.p2e66qxp').get()
        print(ads_list)