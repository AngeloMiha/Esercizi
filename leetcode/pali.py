class Solution(object):
    def isPalindrome( x):
        if x < 0:
            return False
        
        lista = [int(cifra) for cifra in str(x)]
        lista_rev = [int(cifra) for cifra in str(x)]
        lista_rev.reverse()

        for num in lista:
            if lista[num] == lista_rev[num]:
                continue
            else:
                return False
        return True
    

print(Solution.isPalindrome(100))

