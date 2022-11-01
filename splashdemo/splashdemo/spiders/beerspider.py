import scrapy
from scrapy_splash import SplashRequest


class BeerSpider(scrapy.Spider):
    name = 'beer'
##make sure def have same indentation to be inside same class

    def start_requests(self):
        url = 'https://www.beerwulf.com/en-gb/c/mixedbeercases'

        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        products = response.css(
                'a.product.search-product.product-info-container.draught-product.notranslate.pack-product')
        for item in products:
            yield {
            'name': item.css('h4::text').get(),
            'price': item.css('span.price::text').get(),
            }
