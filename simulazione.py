import random

def stampa_percorso(pos_tartaruga, pos_lepre):
    percorso = ['_'] * 70
    if pos_tartaruga == pos_lepre:
        percorso[pos_tartaruga - 1] = 'OUCH!!!'
    else:
        percorso[pos_tartaruga - 1] = 'T'
        percorso[pos_lepre - 1] = 'H'
    print(''.join(percorso))


def mosse_tarta(pos):
    i = random.randint(1, 11)
    if 1 <= i <= 5:
        pos += 3
    elif 6 <= i <= 7:
        if pos != 0 and pos > 6:
            pos -= 6
        else:
            pos = 0
    elif 8 <= i <= 10:
        pos += 1
    if pos > 70:
        pos = 70
    return pos



def mosse_lepre(pos):
    i = random.randint(1, 11)
    if 1 <= i <= 2:
        pos += 0
    elif 3 <= i <= 4:
        pos += 9
    elif i == 5:
        if pos != 1 and pos > 12:
            pos -= 12
        else:
            pos = 0
    elif 6 <= i <= 8:
        pos += 1
    elif 9 <= i <= 10:
        if pos != 1 and pos > 2:
            pos -= 2
        else:
            pos = 0
    if pos > 70:
        pos = 70
    return pos


def gara():
    pos_t = 1
    pos_h = 1
    print("BANG !!! AND THEY'RE OFF !!!")

    while pos_t < 70 or pos_h < 70:
        pos_h = mosse_lepre(pos_h)
        pos_t = mosse_tarta(pos_t)
        stampa_percorso(pos_t, pos_h)

gara()