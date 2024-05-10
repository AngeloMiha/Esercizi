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


# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi.
# Restituisci un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    dizzionario: dict = {}
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            sconto = prezzo * 0.9
            dizzionario[prodotto] = sconto
    return dizzionario
