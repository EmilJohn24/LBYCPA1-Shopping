
def calculation(cart):
    total = 0
    for product in cart:
        total += product['price'] * product['count']
    return total


def summary(cart, info):
    print("Summary of your purchase including inputed personal info")
    for k, v in info.items():
        print(k, v)
    print()
    index = 1
    for product in cart:
        print(f"{index}. {product['name']} - Php {product['price']} - {product['count']} pcs.")
    print("-----------------------------------")
    total = calculation(cart)
    print(f"Total Price: {total}")
    cash = float(input("How much cash will you tender? "))
    payment(cash, total)


def payment(cash, total):
    if cash > total:
        print("Successful transaction")
        print("Change:", total - cash)
    else:
        print("Not enough cash...")

