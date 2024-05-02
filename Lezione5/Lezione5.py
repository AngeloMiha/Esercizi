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

