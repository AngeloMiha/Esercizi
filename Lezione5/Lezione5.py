# Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def rounded_average(numbers: list[int]) -> int:
    somma: int = 0
    med: int = 0
    cont: int = 0
    for num in numbers:
        somma += num
        cont += 1
    med = somma / cont
    return round(med)
print(rounded_average([1, 1, 2, 2]))
