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


# Scrivi una funzione che, dato un numero intero, determina se è un "numero magico".
# Un numero magico è definito come un numero che contiene il numero 7.
def is_magic_number(num: int) -> bool:
    lista: list[int] = []
    for num in str(num):
        lista.append(num)
    
    for number in lista:
        if number == '7':
            return True
        else:
            continue
    return False


# Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
def list_statistics(numbers: list[int]):
    massimo: int = max(numbers)
    minimo: int = min(numbers)
    somma: int = 0
    med: int = 0
    cont: int = 0
    for num in numbers:
        somma += num
        cont += 1
    med = somma / cont
    return massimo, minimo, med


# Il codice dovrebbe stampare i numeri all'interno di una lista.
# TROVA L'ERRORE E CORREGGI IL CODICE
numbers: list[int] = [1, 2, 3, 4, 5]

for i in numbers:
    print("Number:", i)


# Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    somma: int = 0
    for num in numbers:
        if num > threshold:
            somma += num
        else:
            continue
    return somma
print(sum_above_threshold([15, 5, 25], 20))
