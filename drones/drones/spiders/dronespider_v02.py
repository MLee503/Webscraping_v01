import scrapy
from drones.drones.items import DronesscraperItem


class DronespiderSpider(scrapy.Spider):
    name = 'dronespider2'
    start_urls = ['http://jessops.com/drones']

    def parse(self, response):
        item = DronesscraperItem()

    for products in response.css('div.f-grid.prod-row'):

    item['product_name'] = products.css('img::attr(alt)').get()
    item['price'] = products.css('p.price.larger::text').get().replace('£', '')
    item['url'] = products.css('a::attr(href)').get()


                yield item
