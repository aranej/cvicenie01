def pozdrav():
    return "Ahoj, svet!"

def scitaj(a, b):
    return a + b

def odcitaj(a, b):
    return a - b

if __name__ == "__main__":
    print(pozdrav())
    print(f"2 + 3 = {scitaj(2, 3)}")
    print(f"5 - 2 = {odcitaj(5, 2)}")
