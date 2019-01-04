import scrapy
import math

class Mogi(scrapy.Spider):
    name = "mogi"
    PREFIX = 'https://mogi.vn/'
    BASE_URLS = ['https://mogi.vn/ho-chi-minh/thue-nha-dat']      

    def start_requests(self):
        for base_url in self.BASE_URLS:
            yield scrapy.Request( url = base_url, callback = self.parse)
        
    def parse(self, response):
        article_urls = response.css('.list-view .property  .property-title a.link-overlay::attr(href)').extract()
        next_page_url = response.css('.paging .pagination li:last-child a::attr(href)').extract_first()
        for url in article_urls:
            yield scrapy.Request(self.PREFIX + url, callback=self.parse_article)
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_article(self, response):
        article = {}
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

