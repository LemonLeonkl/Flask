import random, string

password_symbols = string.printable


def def_password():
    password = ''
    for i in range(10):
        symbol = random.choice(password_symbols)
        password = password + symbol   
    return password
