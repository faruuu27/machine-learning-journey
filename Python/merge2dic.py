from collections import Counter

def main():

    cart1 = {'apple': 2, 'banana': 1}
    cart2 = {'banana': 3, 'orange': 5}

    combined_cart=dict(Counter(cart1)+Counter(cart2))

    print(combined_cart)

main()