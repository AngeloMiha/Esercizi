cont = 0
i = 0
j = 1
l = [2, 0, 2, 1, 1, 0]
sus = len(l)
print(l)

while cont < len(l)**2:

    if j == sus:
        i = 0
        j = 1
    else:
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j += 1
            cont += 1
        elif l[j] > l[i]:
            i += 1
            j += 1
            cont += 1

print(l)