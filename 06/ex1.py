# print("Mesaj")
# nr1 = input("Adauga un nr: ")

# def my_function():
#     pass

# def suma(c: int, a: int = 2, b: int = 5) -> (int, int):
#     return a + b + c, a - b - c
    # print(f"Suma: {a + b}")


# suma_1 = suma(3)
# suma_1 = suma(10, b=7)
# suma_1,  diferenta_1 = suma(b=7, c=10)
# print(f"Rezultatul este: {suma_1} si diferenta {diferenta_1}")
dict = {'a': 1, "b": 2}


def suma(a=1, b=7, *args, **kwargs):
    """
    :param a: primul parametru
    :param b: al doilea parametru
    :param args:
    :param kwargs:
    :return: suma numarelor
    """
    # print(type(kwargs))
    total = a + b
    # print(type(args))
    for i in args:
        total += i
    for j in kwargs.values():
        total += j
    return total


# suma_1 = suma(1, 2, 3, 4, 5, 6, 7)
suma_1 = suma(1, 7, 3, 4, 5, 6, 7, d=7, e=8)
print(suma_1)
