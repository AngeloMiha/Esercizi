
def subtract(a: float, b: float):
    diff: float = a-b
    return diff
a: float = float(input("Inserisci il primo numero: "))
b: float = float(input("Inserisci il secondo numero: "))
differenza = subtract(a, b)
print(f"La differenza è: ", differenza)

 
"""
l = [3, 7, 8, 4, 1, 6, 3, 8, 4]
def median(l: list[float]):
    l.sort()
    i: float = 0
    for numbers in l:
        i += 1

    if i % 2 == 0:
        i = i//2
        med = (l[i]+l[i+1]) // 2
    else:
        i = i//2
        med = l[i]
    return med

med = median(l)
print(f"La mediana è: {med}")
"""

"""
l = [1, 2, 3, 4, 5, 6]
def diff_cum(l: list[float]):
    cum: float = l[0]
    for number in l[1:]:
        cum -= number
    return cum
print(f"La sottrazione è: {diff_cum(l)}")
"""
