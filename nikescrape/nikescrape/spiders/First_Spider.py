import scrapy


class NikeSpider(scrapy.Spider):
    name = 'nike_fleece'
    start_urls = ['https://www.nike.com/w?q=fleece&vst=fleece']

    # etract - request
    # transform - parse
    # load - output

    def parse(self, response):
        for products in response.css('div.product-card__body'):
            try:
                yield {
                    'name': products.css('a.product-card__link-overlay::text').get(),
                    'sale_price': products.xpath(
                        '//div[@class="product-price is--current-price css-1ydfahe"]/text()').get().replace('$', ""),
                    'regular_price': products.xpath(
                        '//div[@class ="product-price us__styling is--striked-out css-0"]/text()').get().replace('$',
                                                                                                                 ""),
                    'link': products.css('a.product-card__link-overlay').attrib['href']
                }
            except:
                yield {
                    'name': products.css('a.product-card__link-overlay::text').get(),
                    'sale_price': 'sold out',
                    'regular_price': 'sold out',
                    'link': products.css('a.product-card__link-overlay').attrib['href']
                }


