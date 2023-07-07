import requests
from bs4 import BeautifulSoup
import html5lib

import Conversion
import ecommerce_working


headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
flipkart = ''
amazon = ''

name = input("Product Name:\n")
flipkart_price = ecommerce_working.flipkart(name, headers)
amazon_price = ecommerce_working.amazon(name, headers)
# croma_price = ecommerce_working.croma(name, headers)
# print(croma_price)


if flipkart_price == '0':
    print("Flipkart: No product found!")
    flipkart_price = int(flipkart_price)
else:
    print("\nFlipkart Price:", flipkart_price)
    flipkart_price = Conversion.convert(flipkart_price)
if amazon_price == '0':
    print("Amazon: No product found!")
    amazon_price = int(amazon_price)
else:
    print("\nAmazon price: ₹", amazon_price)
    amazon_price = Conversion.convert(amazon_price)
# if croma_price == '0':
#     print("Croma: No product found!")
#     croma_price = int(croma_price)
# else:
#     print("\nCroma Price:", croma_price)
#     croma_price = Conversion.convert(croma_price)


min_price = min(amazon_price, flipkart_price)
str(min_price)
print(type(min_price))
exit()
print("The best deal for \t" + name + "is" + min_price)
print(min_price)

if min_price == amazon_price:
    print('The Minimum price of' + name + 'is at amazon and is' + str(amazon_price))
    print(amazon)
else:
    print('The Minimum price of' + name + 'is at flipkart and is' + str(flipkart_price))
    print(flipkart)


