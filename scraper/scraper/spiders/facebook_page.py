import scrapy
from urllib.parse import urlencode

API = ''

def get_url(url):
    payload = {'api_key': API, 'proxy': 'datacenter', 'timeout': '20000', 'url': url}
    proxy_url = 'https://api.webscraping.ai/html?' + urlencode(payload)
    return proxy_url


class facebook_page(scrapy.Spider):
    name = 'facebook_page'
    #allowed_domains = ['api.webscraping.ai']
    custom_settings = {'CONCURRENT_REQUESTS_PER_DOMAIN': 5}

    def start_requests(self):
        url = 'https://www.facebook.com/smithgillarch/'
        print("new url", get_url(url))
        print('normal url', url)
        yield scrapy.Request(url, callback=self.parse, meta={'pos': 0})



    def parse(self, response):
        print("parse live2")
        #print(get_posts('smithgillarch', pages=10))
        posts = response.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv') #x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz.x1gslohp.x1yc453h
        print(posts)
        #response.css('.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz.x1gslohp.x1yc453h')
        for post in posts:
            facebook_post_like = post.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv span.nnzkd6d7::text').get()
            com_share = post.css('.dkzmklf5 span::text').get()
            print("fb_like",facebook_post_like," comment",com_share)
        #post .g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv
        #comment response.css('.dkzmklf5 span::text').get()
        #share or comment
        #facebook_post_like = response.css('.g4tp4svg.mfclru0v.om3e55n1.p8bdhjjv span.nnzkd6d7::text').get()
        #for each post =