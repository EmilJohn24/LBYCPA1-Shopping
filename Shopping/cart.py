import products
import checkout

# changed cart format to {"name": name, "price": price, "count": count} for convenience

"""
    In principle, global variables are a terrible idea but this will not be exported into the global namespace and
     will remain in the cart.py namespace to maintain integrity if the program were scaled. (it won't)
"""
cart = []


def display_cart():
    for index, product in enumerate(cart):
        print(f"{index}. {product['name']} - {product['count']} pcs.")


def buy():
    categories = products.display_categories()
    category = products.get_category_from_user(categories)
    products.display_products_from(category)
    item = int(input("Choose a product: "))
    count = int(input("How many? "))
    add_product(item, category, count)


def add_product(item_number, category_list, count):
    new_count = category_list[item_number]['stock'] - count
    if new_count <= 0:
        print('Out of stock')
        buy()
    category_list[item_number]['stock'] = new_count
    cart.append(category_list[item_number])
    cart[len(cart) - 1]['count'] = count


def remove_product(cart_number, count):
    cart[cart_number]['count'] = cart[cart_number]['count'] - count
    if cart[cart_number]['count'] <= 0:
        del cart[cart_number]


def take_user_action(info):
    print("What do you wish to do?")
    print("1-Add More Products To Cart <3")
    print("2-Remove Products From Cart :(")
    print("3-Checkout <3 <3")
    choice = int(input("Your choice: "))

    if choice == 1:
        buy()
        take_user_action(info)
    # if the user chose to remove something
    if choice == 2:
        display_cart()
        cart_number = int(input("Type the number of the product you'd like removed: "))
        count = int(input("How many would you like to remove: "))
        remove_product(cart_number, count)
        take_user_action(info)
    if choice == 3:
        checkout.summary(cart, info)
