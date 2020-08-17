import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
                
    
    def parse_details(self, response):
        yield{
            'name': response.css('h3.author-title::text').extract_first(),
            'birth-date': response.css('span.author-born-date::text').extract_first(),
        }
#response.css('div.oneByone > a::attr(href)').extract()[0]
