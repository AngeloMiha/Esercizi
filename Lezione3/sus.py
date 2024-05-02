def prime_factors(n: int) -> list[int]:
    lista: list[int] = []
    while n != 1:
        if n % 2 == 0:
            lista.append(2)
            n = n / 2
        elif n % 3 == 0:
            lista.append(3)
            n = n / 3
        elif n % 5 == 0:
            lista.append(5)
            n = n / 5
        elif n % 7 == 0:
            lista.append(7)
            n = n / 7
        elif n % 11 == 0:
            lista.append(11)
            n = n / 11
        else:
            lista.append(n)
            n = 1
    return lista
print(prime_factors(99999999999999999999))
