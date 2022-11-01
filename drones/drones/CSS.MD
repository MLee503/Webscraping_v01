#CSS Selectors

url = https://www.jessops.com/drones

products = response.css('div.f-grid.prod-row')

price = products.css('p.price.larger::text').get()

href = products.css('a::attr(href)').get()

product_name = products.css('img::attr(alt)').get()


