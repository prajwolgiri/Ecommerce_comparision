lst = [flipkart_price, amazon_price]
# print(lst)
lst2 = []
for j in range(0, len(lst)):
    if lst[j] > 0:
        lst2.append(lst[j])
if len(lst2) == 0:
    print("No relative product find in all websites....")
else:
    min_price = min(lst2)

    print("_______________________________")
    print("\nMinimun Price: ₹", min_price)
    price = {
        f'{amazon_price}': f'{amazon}',
        f'{flipkart_price}': f'{flipkart}',
    }
    for key, value in price.items():
        if int(key) == min_price:
            print('\nURL:', price[key], '\n')

    print(
        "---------------------------------------------------------URLs--------------------------------------------------------------")
    print("Flipkart : \n", flipkart)
    print("\nAmazon : \n", amazon)
    print(
        "---------------------------------------------------------------------------------------------------------------------------")