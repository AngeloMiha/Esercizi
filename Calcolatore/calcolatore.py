import math

class Calculator:

    def __init__(self) -> None:
        self.num = 0

    def add(self, num):
        sus = self.num
        self.num += num
        return f"{sus} + {num} = {self.num}"
    
    def sub(self, num):
        sus = self.num
        self.num -= num
        return f"{sus} - {num} = {self.num}"
    
    def mult(self, num):
        sus = self.num
        self.num = self.num * num
        return f"{sus} * {num} = {self.num}"
    
    def div(self, num):
        sus = self.num
        if num == 0:
            return f"Impossibile dividere per 0."
        else:
            self.num = self.num / num
        return f"{sus} / {num} = {self.num}"
    
    def percent(self):
        sus = self.num
        self.num = self.num /100
        return f"{sus}% = {self.num}"
    
    def radice(self):
        sus = self.num
        self.num = math.sqrt(self.num)
        return f"√({sus}) = {self.num}"
    
    def quad(self):
        sus = self.num
        self.num = self.num * self.num
        return f"{sus} * {sus} = {self.num}"
    
    def reset(self):
        self.num = 0
        return self.num
    
    def canc(self):
        numero_str = str(self.num)
        
        if numero_str == '0':
            self.num = 0
            return self.num

        negativo = False
        if numero_str.startswith('-'):
            negativo = True
            numero_str = numero_str[1:]  
        
        numero_str = numero_str[:-1]
        
        if numero_str == '':
            self.num = 0
        else:
            self.num = float(numero_str) if '.' in numero_str else int(numero_str)
            if negativo:
                self.num = -self.num
        
        return self.num


    

def test_calculator():
    calc = Calculator()

    # Test di addizione
    print("Addizione:", calc.add(10))
    print("Addizione:", calc.add(5)) 

    # Test di sottrazione
    print("Sottrazione:", calc.sub(3))

    # Test di moltiplicazione
    print("Moltiplicazione:", calc.mult(2))

    # Test di divisione
    print("Divisione:", calc.div(4))

    # Test di percentuale
    print("Percentuale:", calc.percent())

    # Test di radice
    print("Radice:", calc.radice())

    # Test di quadrato
    print("Quadrato:", calc.quad())

    # Test di reset
    print("Reset:", calc.reset())
    # Test di cancellazione
    calc.num = 123.45
    print("Cancella:", calc.canc())

    calc.num = 0.45
    print("Cancella:", calc.canc())

    calc.num = 0
    print("Cancella:", calc.canc())
    calc.num = -123.45
    print("Cancella:", calc.canc())

test_calculator()
