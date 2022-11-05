import scrapy


class DronespiderSpider(scrapy.Spider):
    name = 'dronespider'
    allowed_domains = ['jessops.com']
    start_urls = ['http://jessops.com/drones']

    def parse(self, response):
        products = response.css('div.f-grid.prod-row')
        for product in products:
            item = {
            'product_name' : product.css('img::attr(alt)').get(),
            'price' : product.css('p.price.larger::text').get().replace('£', ''),
            'url' : product.css('a::attr(href)').get()
            }

            yield item
        pass

