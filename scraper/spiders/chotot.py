
# MISSION IMPOSSIBLE ~~

# import scrapy
# import math

# class Mogi(scrapy.Spider):
#     name = "chotot"
#     PREFIX = 'https://nha.chotot.com/'
#     CURRENT_DOMAIN = 'HCM-mua-nha'
#     CURRENT_URL = ''
#     BASE_URLS = dict()

#     BASE_URLS['HCM-mua-ban-can-ho-chung-cu'] = 'https://nha.chotot.com/tp-ho-chi-minh/mua-ban-can-ho-chung-cu'
#     # BASE_URLS['HCM-mua-ban-nha-dat'] = 'https://nha.chotot.com/tp-ho-chi-minh/mua-ban-nha-dat'
#     # BASE_URLS['HCM-mua-ban-dat'] = 'https://nha.chotot.com/tp-ho-chi-minh/mua-ban-dat'
#     # BASE_URLS['HCM-sang-nhuong-van-phong-mat-bang-kinh-doanh'] = 'https://nha.chotot.com/tp-ho-chi-minh/sang-nhuong-van-phong-mat-bang-kinh-doanh'

#     # BASE_URLS['HCM-thue-can-ho-chung-cu'] = 'https://nha.chotot.com/tp-ho-chi-minh/thue-can-ho-chung-cu'
#     # BASE_URLS['HCM-thue-nha-dat'] = 'https://nha.chotot.com/tp-ho-chi-minh/thue-nha-dat'
#     # BASE_URLS['HCM-thue-dat'] = 'https://nha.chotot.com/tp-ho-chi-minh/thue-dat'
#     # BASE_URLS['HCM-thue-van-phong-mat-bang-kinh-doanh'] = 'https://nha.chotot.com/tp-ho-chi-minh/thue-van-phong-mat-bang-kinh-doanh'
#     # BASE_URLS['HCM-thue-phong-tro'] = 'https://nha.chotot.com/tp-ho-chi-minh/thue-phong-tro'

#     # BASE_URLS['HN-mua-ban-can-ho-chung-cu'] = 'https://nha.chotot.com/ha-noi/mua-ban-can-ho-chung-cu'
#     # BASE_URLS['HN-mua-ban-nha-dat'] = 'https://nha.chotot.com/ha-noi/mua-ban-nha-dat'
#     # BASE_URLS['HN-mua-ban-dat'] = 'https://nha.chotot.com/ha-noi/mua-ban-dat'
#     # BASE_URLS['HN-sang-nhuong-van-phong-mat-bang-kinh-doanh'] = 'https://nha.chotot.com/ha-noi/sang-nhuong-van-phong-mat-bang-kinh-doanh'

#     # BASE_URLS['HN-thue-can-ho-chung-cu'] = 'https://nha.chotot.com/ha-noi/thue-can-ho-chung-cu'
#     # BASE_URLS['HN-thue-nha-dat'] = 'https://nha.chotot.com/ha-noi/thue-nha-dat'
#     # BASE_URLS['HN-thue-dat'] = 'https://nha.chotot.com/ha-noi/thue-dat'
#     # BASE_URLS['HN-thue-van-phong-mat-bang-kinh-doanh'] = 'https://nha.chotot.com/ha-noi/thue-van-phong-mat-bang-kinh-doanh'
#     # BASE_URLS['HN-thue-phong-tro'] = 'https://nha.chotot.com/ha-noi/thue-phong-tro'


#     def start_requests(self):
#         for domain, base_url in self.BASE_URLS.items():
#             self.CURRENT_DOMAIN = domain
#             self.CURRENT_BASE_URL = base_url
#             print("CRAWL DATA IN DOMAIN: ", domain.upper(), '\n')
#             yield scrapy.Request(url = base_url, callback = self.parse_url)


#     def parse_url(self, response):
#         article_urls = response.css('.-AGAL8Zp7YDoV-PVebFY0 ._3qr34_XMQROJG0YnuXtt9c a._3JMKvS6hucA6KaM9tX3Qb1::attr(href)').extract()
#         print('HAHAHAHAHAHAHAHAHAHAHA', response.headers)
#         for url in article_urls:
#             self.CURRENT_URL = self.PREFIX + url
#             yield scrapy.Request(url = self.CURRENT_URL, callback=self.parse_article)

#         # next_page_url = response.css('.sc-fAjcbJ .sc-caSCKo li:last-child a::attr(href)').extract_first()
#         # if next_page_url is not None:
#         #     print("BASE URL: ", next_page_url.upper(), '\n')
#         #     yield scrapy.Request(next_page_url, callback=self.parse_url)

#     def parse_article(self, response):
#         article = dict()
#         article['domain'] = self.CURRENT_DOMAIN
#         article['url'] = self.CURRENT_URL
#         article['tittle']           = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/h1/text()').extract()[0].strip()      
#         article['address']          = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/text()').extract()[0].strip()
#         article['price']            = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/text()').extract()[0].strip()
#         article['usable_area']      = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]/text()[2]').extract()[0].strip()
#         # article['area']             = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[3]/text()').extract()[0].strip()
#         # article['publish_date']     = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[4]/text()').extract()[0].strip()
#         # article['real_estate_id']   = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[5]/text()').extract()[0].strip()
#         # article['bedroom']          = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div/span/text()[3]').extract()[0].strip()
#         # article['bathroom']         = response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[5]/div/span/text()[3]').extract()[0].strip()
#         # article['legal_papers']     = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[3]/text()').extract()[0].strip()
#         # article['direction']        = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[4]/text()').extract()[0].strip()
#         article['description']      = "\n".join(response.xpath('//*[@id="app"]/div[2]/main/article/div[1]/div[2]/div[1]/div[2]/p/text()').extract()).strip()
#         # for key, text in article.items():
#         #     print("{key}: {text}".format(key = key.upper(), text = text))

#         return article

