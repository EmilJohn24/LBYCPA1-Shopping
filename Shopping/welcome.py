def get_info(info: dict):
    """

    :param info: A dictionary that will serve as the placeholder for the user's name and email address
    :return:
    """
    print("Welcome to Power Mark Center!")
    print("Where Everyone Le-stares At You")
    info["name"] = input("Please input your name: ")
    info["email"] = input("Please input your email address to receive a copy of your receipt: ")


def loader(length):
    i = 0
    print("Loading...", end="")
    while i <= length:
        delay = range(0, 1000000)
        for num in delay:
            a = 2
        print("█", end="")
        # command = "timeout /t 200 /NOBREAK"
        # os.system(command)
        i += 1
    print("\nDone...")
