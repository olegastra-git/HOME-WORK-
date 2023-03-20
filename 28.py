a = int(input(" vvedite chislo a: - "))
b = int(input(" vvedite chislo b: - "))


def summa(a, b):
    return summa(a + 1, b - 1) if b > 0 else a


print sum(a, b)
