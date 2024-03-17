product_name = str(input('What do you want to buy? '))
product_price_og = int(input('Enter the price of the product you want to buy in pence (e.g. 185 and 1 pound = 100p): '))
product_number = int(input('Enter the quantity of ' + product_name + ' you want to buy: '))
product_price_pence = product_price_og * product_number
product_price_pound = product_price_pence // 100
product_price_pound_rest = product_price_pence % 100
print(product_number,product_name,'will cost you',product_price_pound,'pounds and',product_price_pound_rest,'pence.')
