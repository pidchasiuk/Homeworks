casino_blacklist = [
    "Deborah Thoennes",
    "Ernest Taylor",
    "Lois Martin",
    "Ruthie Mcclendon"
]

poker_blacklist = [
    "Clyde Guajardo",
    "Cynthia Marshall",
    "Nadine Huges",
    "Lois Martin",
    "Alice Whatoname"
]

alcohol_blacklist = [
    "Gladys Price",
    "Theodore Owens",
    "Alice Whatoname",
]


def check_casino(name):
    if name in casino_blacklist:
        return True
    else:
        return False


def check_poker(name):
    if name in poker_blacklist:
        return True
    else:
        return False


def check_alcohol(name):
    if name in alcohol_blacklist:
        return True
    else:
        return False


if __name__ == "__main__":
    name_inp = input("Input a name: ").title()

    if len(name_inp.split(" ")) == 2:
        print(f'User is in casino blacklist: {check_casino(name_inp)}\n'
              f'User is in poker blacklist: {check_poker(name_inp)}\n'
              f'User is in alcohol blacklist: {check_alcohol(name_inp)}')
    else:
        print('ERROR: incorrect name format. Have to be like "John Dow"')
