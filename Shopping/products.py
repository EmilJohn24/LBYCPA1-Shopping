def product(name, price, stock):
    prod = {"name": name, "price": price, "stock": stock}
    return prod


"""
    In principle, global variables are a terrible idea but this will not be exported into the global namespace and 
     will remain in the products.py namespace to maintain integrity if the program were scaled. (it won't)
"""
products = {


    "Phones": [product("iPhone 7 Plus", 29990, 30), product("iPhone8", 39490, 50),       product("iPhoneXR", 50990, 100),
               product("iPhoneXs", 67990, 150), product("iPhoneXs Marks", 79990, 150)],
    "Earphones": [product("AirPods  ", 7451, 250), product("EarPods", 1790, 200)],
    "Laptops": [product("Markbook Air", 86990, 100), product("Markbook", 94990, 100),
                product("Markbook Pro", 173990, 50)],
    "Watch": [product("Apple Watch Series 3", 17990, 100), product("Apple Watch Series 2", 13990, 100)],
    "Tablets": [product("iPadilla Pro", 42490, 30), product("iPadilla", 20990, 50), product("iPadilla Mini 4", 23990, 50)],
}


def get_products_in(category):
    return products[category]


def display_categories():
    categories = []  # List for category names to be used for quick index lookup of categories in get_category_from_user
    for index, category in enumerate(products.keys()):
        categories.append(category)
        print("{0}. {1}".format(index, category))
    return categories


def get_category_from_user(categories):
    category = int(input("Type the number of your category: "))
    return products[categories[category]]


def display_products_from(category):
    for index, item in enumerate(category):
        print(f"{index}. {item['name']} -- {item['price']}")




