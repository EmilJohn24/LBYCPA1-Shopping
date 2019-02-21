def get_info(info: dict):
    """

    :param info: A dictionary that will serve as the placeholder for the user's name and email address
    :return:
    """
    print("Welcome to Power Mark Center!")
    print("Where Everyone Le-stares At You")
    info["name"] = input("Please input your name: ")
    info["email"] = input("Please input your email address to receive a copy of your receipt: ")