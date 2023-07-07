import requests
from bs4 import BeautifulSoup

def flipkart(name, headers):
    try:
        global flipkart
        name1 = name.replace(" ", "+")
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text, 'html.parser')

        if (soup.select('._4rR01T')):
            flipkart_name = soup.select('._4rR01T')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('._4rR01T')[0].getText().strip()
                print("Flipkart:")
                print(flipkart_name)
                print(flipkart_price)
                print("---------------------------------")

        elif (soup.select('.s1Q9rs')):
            flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
            flipkart_name = flipkart_name.upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
                print("Flipkart:")
                print(flipkart_name)
                print(flipkart_price)
                print("---------------------------------")
        else:
            flipkart_price = '0'

        return flipkart_price
    except:
        print("Flipkart: No product found!")
        print("---------------------------------")
        flipkart_price = '0'
    return flipkart_price


def amazon(name, headers):
    try:
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'

        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
        print("\nSearching in amazon...")
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0, amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                print(amazon_name)
                print("₹" + amazon_price)
                print("---------------------------------")
                break
            else:
                i += 1
                i = int(i)
                if i == amazon_page_length:
                    amazon_price = '0'
                    print("amazon : No product found!")
                    print("-----------------------------")
                    break

        return amazon_price
    except:
        print("Amazon: No product found!")
        print("---------------------------------")
        amazon_price = '0'
    return amazon_price

# def croma(name, headers):
#     try:
#         global croma
#         name1 = name.replace(" ","+")
#         croma = f'https://www.croma.com/search/?text={name1}'
#         res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)
#
#         soup = BeautifulSoup(res.text,'html.parser')
#         croma_name = soup.select('h3')
#
#         croma_page_length = int( len(croma_name))
#         for i in range (0,croma_page_length):
#             name = name.upper()
#             croma_name = soup.select('h3')[i].getText().strip().upper()
#             if name in croma_name.upper()[:25]:
#                 croma_name = soup.select('h3')[i].getText().strip().upper()
#                 croma_price = soup.select('.pdpPrice')[i].getText().strip()
#
#                 break
#             else:
#                 i+=1
#                 i=int(i)
#                 if i==croma_page_length:
#
#                     croma_price = 'Product Not Found'
#                     break
#
#         return f"{croma_name}\nPrise : {croma_price}\n"
#     except:
#
#         croma_price = '  Product Not Found'
#     return croma_price