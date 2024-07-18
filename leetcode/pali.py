class Solution(object):
    def isPalindrome( x):
        if x < 0:
            return False
        
        lista = [int(cifra) for cifra in str(x)]
        lista_rev = [int(cifra) for cifra in str(x)]
        lista_rev.reverse()

        if lista == lista_rev:
            return True
        return False
    

print(Solution.isPalindrome(100))

