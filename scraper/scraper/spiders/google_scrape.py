import scrapy
import xlsxwriter
import logging
class firstSpider(scrapy.Spider):
    name = 'companies'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_companies_in_the_Chicago_metropolitan_area']

    def __init__(self):
        self.workbook = xlsxwriter.Workbook('businesses_test.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.write('A1', 'Links')
   # self.worksheet = worksheet
    i = 0
    big_chunky_list =[]
    def parse(self, response):
        print("called parse")
        items =   response.css('div[class=div-col] a::attr(href)').getall()
        for item in items:
            self.i += 1
            print("called item in items : ",self.i)
            if "https://en.wikipedia.org" not in item:
                item="https://en.wikipedia.org"+item
                link = response.urljoin(item)

            yield scrapy.Request(url=link, callback=self.parse_businesses)


    def parse_businesses(self,response):
        print("called parse businesses")
        try:
            page_link = response.css('span[class=url] a::attr(href)').get()
            link = response.urljoin(page_link)
            try:
                self.add_business(self.big_chunky_list, page_link)

            except Exception as e:
                print("error is : ", e)
          #  yield scrapy.Request(url=link, callback=self.parse_business)
        except Exception as e:
            print(e)



    # def parse_business(self,response):
    #     print("parse business")
    #     try:
    #
    #         hrefs_xpath = "//a/@href[contains(., 'business') or contains(.,'brand')]"
    #         #print(hrefs_xpath)
    #         contact_info = response.xpath(hrefs_xpath).extract()
    #         print("contact info is ",contact_info)
    #        # print(website_link)
    #         #yield scrapy.Request(url=contact_info, callback=self.parse_contact_page)
    #     except Exception as e:
    #         print(e)

        #print("contact info",contact_info)


    # def parse_contact_page(self,response):
    #     print("contact page welcome")
    #
    # print("end of code")
    # for chunk in big_chunky_list:
    #     i+=1
    #     print(chunk)
    #     worksheet.write('A1' + i, chunk)


    def add_business(self,list,link):
        print("list ",list)
        try:
            self.i+=1
            list.append(link)
            new_business = Business()
            new_business.link=link
            new_business.phone_number=""
            new_business.address=""
            self.worksheet.write('B' + str(self.i), link)
            self.worksheet.write('C'+ str(self.i), "phone")
            self.worksheet.write('D'+ str(self.i), "address")
        except Exception as e:
            print(e)


    def closed(self, reason):
        self.workbook.close()
        logging.info("Closed book")

class Business:
    link =""
    phone_number=""
    address=""
