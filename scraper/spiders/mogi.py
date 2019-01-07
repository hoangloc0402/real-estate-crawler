import scrapy
import math

class Mogi(scrapy.Spider):
    name = "mogi"
    PREFIX = 'https://mogi.vn/'
    CURRENT_DOMAIN = 'HCM-mua-nha'
    CURRENT_URL = ''
    BASE_URLS = dict()

    # BASE_URLS['HCM-mua-nha'] = 'https://mogi.vn/ho-chi-minh/mua-nha'
    # BASE_URLS['HCM-mua-can-ho'] = 'https://mogi.vn/ho-chi-minh/mua-can-ho'
    # BASE_URLS['HCM-mua-dat'] = 'https://mogi.vn/ho-chi-minh/mua-dat'
    # BASE_URLS['HCM-mua-mat-bang-cua-hang-shop'] = 'https://mogi.vn/ho-chi-minh/mua-mat-bang-cua-hang-shop'

    # BASE_URLS['HCM-thue-nha'] = 'https://mogi.vn/ho-chi-minh/thue-nha'
    # BASE_URLS['HCM-thue-can-ho'] = 'https://mogi.vn/ho-chi-minh/thue-can-ho'
    # BASE_URLS['HCM-thue-phong-tro-nha-tro'] = 'https://mogi.vn/ho-chi-minh/thue-phong-tro-nha-tro'
    # BASE_URLS['HCM-thue-van-phong'] = 'https://mogi.vn/ho-chi-minh/thue-van-phong'
    # BASE_URLS['HCM-thue-mat-bang-cua-hang-shop'] = 'https://mogi.vn/ho-chi-minh/thue-mat-bang-cua-hang-shop'
    # BASE_URLS['HCM-thue-nha-xuong-kho-bai-dat'] = 'https://mogi.vn/ho-chi-minh/thue-nha-xuong-kho-bai-dat'

    # BASE_URLS['HN-mua-nha'] = 'https://mogi.vn/ha-noi/mua-nha'
    # BASE_URLS['HN-mua-can-ho'] = 'https://mogi.vn/ha-noi/mua-can-ho'
    # BASE_URLS['HN-mua-dat'] = 'https://mogi.vn/ha-noi/mua-dat'
    BASE_URLS['HN-mua-mat-bang-cua-hang-shop'] = 'https://mogi.vn/ha-noi/mua-mat-bang-cua-hang-shop'

    # BASE_URLS['HN-thue-nha'] = 'https://mogi.vn/ha-noi/thue-nha'
    # BASE_URLS['HN-thue-can-ho'] = 'https://mogi.vn/ha-noi/thue-can-ho'
    # BASE_URLS['HN-thue-phong-tro-nha-tro'] = 'https://mogi.vn/ha-noi/thue-phong-tro-nha-tro'
    # BASE_URLS['HN-thue-van-phong'] = 'https://mogi.vn/ha-noi/thue-van-phong'
    # BASE_URLS['HN-thue-mat-bang-cua-hang-shop'] = 'https://mogi.vn/ha-noi/thue-mat-bang-cua-hang-shop'
    # BASE_URLS['HN-thue-nha-xuong-kho-bai-dat'] = 'https://mogi.vn/ha-noi/thue-nha-xuong-kho-bai-dat'


    def start_requests(self):
        for domain, base_url in self.BASE_URLS.items():
            self.CURRENT_DOMAIN = domain
            print("CRAWL DATA IN DOMAIN: ", domain.upper(), '\n')
            yield scrapy.Request(url = base_url, callback = self.parse_url)
        
    def parse_url(self, response):
        article_urls = response.css('.props .prop-title a.link-overlay::attr(href)').extract()
        next_page_url = response.css('.paging .pagination li:last-child a::attr(href)').extract_first()
        for url in article_urls:
            self.CURRENT_URL = self.PREFIX + url
            yield scrapy.Request(self.CURRENT_URL, callback=self.parse_article)

        if next_page_url is not None:
            print("BASE URL: ", next_page_url.upper(), '\n')
            yield scrapy.Request(next_page_url, callback=self.parse_url)


    def parse_article(self, response):
        print("HIhihihihihihi",response)
        article = dict()
        article['domain'] = self.CURRENT_DOMAIN
        article['url'] = self.CURRENT_URL

        # article['tittle']           = response.xpath('//*[@id="property"]/div[1]/div[1]/h1/text()').extract()[0].strip()      
        # article['address']          = response.xpath('//*[@id="property"]/div[1]/div[1]/div[1]/text()').extract()[0].strip()
        article['price']            = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[1]/text()').extract()[0].strip()
        article['usable_area']      = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[2]/text()').extract()[0].strip()
        article['area']             = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[3]/text()').extract()[0].strip()
        article['publish_date']     = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[4]/text()').extract()[0].strip()
        article['real_estate_id']   = response.xpath('//*[@id="property-info"]/div[1]/ul[1]/li[5]/text()').extract()[0].strip()
        article['bedroom']          = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[1]/text()').extract()[0].strip()
        article['bathroom']         = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[2]/text()').extract()[0].strip()
        article['legal_papers']     = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[3]/text()').extract()[0].strip()
        article['direction']        = response.xpath('//*[@id="property-info"]/div[1]/ul[2]/li[4]/text()').extract()[0].strip()
        article['description']      = "\n".join(response.xpath('//*[@id="property-info"]/div[2]/text()').extract()).strip()

        for key, text in article.items():
            print("{key}: {text}".format(key = key.upper(), text = text))

        return article

