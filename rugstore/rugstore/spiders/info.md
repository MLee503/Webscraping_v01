# CSS selector

next_page = response.css('a[title=Next]::attr(href)').get()

allproducts = response.xpath('//li[@class="item product product-item"]')

price = response.css('span.price::text').get()

hyperlink = response.css('a.product-item-link::attr(href)').get()
 
product_name = response.css('img.product-image-photo.image::attr(alt)').get()


