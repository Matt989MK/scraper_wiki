# import scrapy
# import logging
# import urllib
# import pandas as pd
# import csv
# import traceback
# import re
# import sys
# from urllib.parse import urlencode
#
# from urllib.parse import urlparse
#
# import json
#
# from datetime import datetime
# API_KEY = 'YOUR_API_KEY'
# class __main__():
#
#     city=input("enter the city: ")
#     niche=input("enter the niche: ")
#
#     def create_google_url(query, site=''):
#
#                     google_dict = {'q': query, 'num': 100, }
#
#                     if site:
#                             web = urlparse(site).netloc
#
#                             google_dict['as_sitesearch'] = web
#
#                             return 'http://www.google.com/search?' + urlencode(google_dict)
#
#                     return 'http://www.google.com/search?' + urlencode(google_dict)
#
#     def get_url(url):
#
#         payload = {'api_key': API_KEY, 'url': url, 'autoparse': 'true', 'country_code': 'us'}
#
#         proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
#
#         return proxy_url