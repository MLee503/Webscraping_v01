
products = response.css('a.product.search-product.product-info-container.draught-product.notranslate.pack-product')

names = products.css('h4.product-name::text').get()

price = products.css('span.price::text').get()

