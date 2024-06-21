class Solution:
    def intToRoman(self, num: int) -> str:
        lista: list[str] = []
        while num > 0:
            if num >= 1000:
                num -= 1000
                lista.append("M")
            elif 500 <= num and num <= 999:
                num_str = str(num)
                sotto_str = str(9)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num -= 900
                    lista.append("CM")
                else:
                    num -= 500
                    lista.append("D")
            elif 100 <= num and num <= 499:
                num_str = str(num)
                sotto_str = str(4)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num -= 400
                    lista.append("CD")
                else:
                    num -= 100
                    lista.append("C")
            elif 50 <= num and num <= 99:
                num_str = str(num)
                sotto_str = str(9)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num -= 90
                    lista.append("XC")
                else:
                    num -= 50
                    lista.append("L")
            elif 10 <= num and num <= 49:
                num_str = str(num)
                sotto_str = str(4)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num -= 40
                    lista.append("XL")
                else:
                    num -= 10
                    lista.append("X")
            elif 5 <= num and num <= 9:
                num_str = str(num)
                sotto_str = str(9)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num-= 9
                    lista.append("IX")
                else:
                    num -= 5
                    lista.append("V")
            elif 1 <= num and num <= 4:
                num_str = str(num)
                sotto_str = str(4)
                indice = num_str.find(sotto_str)
                if indice == 0:
                    num -= 4
                    lista.append("IV")
                else:
                    num -= 1
                    lista.append("I")
        num_romani = "".join(lista)
        return num_romani

sus = Solution
print(sus.intToRoman(3749))
