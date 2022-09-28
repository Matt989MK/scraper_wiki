import scrapy
from urllib.parse import urlencode
from facebook_scraper import get_posts

#API = '18fa7b1832038d45d7c56aa19587272a'
API = 'e5d9f2d2-58ea-4e33-8f6e-ef9fbb67908d'

def get_url(url):
    payload = {'api_key': API, 'proxy': 'datacenter', 'timeout': '20000', 'url': url}
    proxy_url = 'https://api.webscraping.ai/html?' + urlencode(payload)
    #print(proxy_url)
    return proxy_url


class facebook_page(scrapy.Spider):
    name = 'facebook_page'
    #allowed_domains = ['api.webscraping.ai']
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 5}

    def start_requests(self):
        url = 'https://www.facebook.com/smithgillarch/'
        print("new url", get_url(url))
        print('normal url', url)
        yield scrapy.Request(get_url(url), callback=self.parse, meta={'pos': 0})



    def parse(self, response):
        print("parse live2")
        #print(get_posts('smithgillarch', pages=10))
        posts = response.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv')
        print(posts)
        for post in posts:
            facebook_post_like = post.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv span.nnzkd6d7::text').get()
            com_share = post.css('.dkzmklf5 span::text').get()
            print("fb_like",facebook_post_like," comment",com_share)
        #post .g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv
        #comment response.css('.dkzmklf5 span::text').get()
        #share or comment
        #facebook_post_like = response.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv span.nnzkd6d7::text').get()
        #for each post =