def pozdrav():
    return "Ahoj, svet!"

def scitaj(a, b):
    return a + b

def odcitaj(a, b):
    return a - b

def nasob(a, b):
    return a * b

def delit(a, b):
    if b == 0:
        return "Nemôžeme deliť nulou!"
    return a / b

if __name__ == "__main__":
    print(pozdrav())
    print(f"2 + 3 = {scitaj(2, 3)}")
    print(f"5 - 2 = {odcitaj(5, 2)}")
    print(f"4 * 3 = {nasob(4, 3)}")
    print(f"10 / 2 = {delit(10, 2)}")
