# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
def list_statistics(numbers: list[int]) -> int:
    massimo: int = 0
    minimo: int = 0
    massimo = max(numbers)
    minimo = min(numbers)   
    media: int = 0
    somma: int = 0
    for num in numbers:
        somma += num
    media = somma / len(numbers)
    return massimo, minimo, media

# Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
def countdown(n: int) -> int:
    print(n)
    while n != 0:
        for i in range(n):
            n -= 1
            print(n)
