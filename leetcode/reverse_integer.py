class Solution(object):
    def reverse(self, x):

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if x == 0:
            return 0
        
        if x < 0:
            neg = True
            x += -(x)*2
            lista = [int(cifra) for cifra in str(x)]
        else:
            neg = False
            lista = [int(cifra) for cifra in str(x)]
        lista.reverse()
        

        sus = True
        while sus == True:
            if lista[-1] == 0:
                lista.remove(lista[-1])
            else:
                sus = False
        x = int(''.join(map(str, lista)))


        if x < INT_MIN or x > INT_MAX:
            return 0


        if neg == True:
            return -(x)
        else:
            return x


print(Solution.reverse(98139139))

