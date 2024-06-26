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


# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
# ritorni un nuovo insieme senza i numeri specificati nella lista.
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for num in elements_to_remove:
        original_set.discard(num)
    return original_set


# Scrivi una funzione che rimuove tutti i duplicati da una lista,
# contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
def remove_duplicates(lista1: list[int]) -> list:
    lista2: list[int] = []
    for num in lista1:
        if num not in lista2:
            lista2.append(num)
    return lista2


# Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
def check_parentheses(expression: str) -> bool:
    lista: list[int] = []
    for i in expression:
        if i == '(':
            lista.append(i)
        elif i == ')':
            if not lista:
                return False
            lista.pop()
    return not lista


# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3: dict = {}
    for k,v in dict1.items():
        if k in dict2:
            dict1[k] += dict2[k]
    
    for k,v in dict1.items():
        dict2[k] = v
    s = sorted(dict2.items())
    for k,v in s:
        dict3[k] = v
    return dict3


# Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
# Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
def count_isolated(lista: list[int]) -> int:
    isolati = 0
    
    if lista == []:
        return isolati
    else:

        if lista[0] != lista[1]:
            isolati += 1
        if lista[-1] != lista[-2]:
            isolati += 1

        for i in range(1, len(lista) - 1):
            if lista[i] != lista[i + 1] and lista[i] != lista[i - 1]:
                isolati += 1
        return isolati
