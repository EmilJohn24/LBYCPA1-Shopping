from os import system
import products
import cart
import welcome

info = {}
welcome.get_info(info)
cart.buy()
welcome.loader(50)
cart.take_user_action()