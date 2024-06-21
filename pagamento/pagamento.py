class Pagamento:
    def __init__(self):
        self.__importo = 0.0

    def get_importo(self):
        return self.__importo

    def set_importo(self, importo):
        if isinstance(importo, (int, float)) and importo >= 0:
            self.__importo = float(importo)
        else:
            raise ValueError("L'importo deve essere un numero non negativo.")

    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.__importo:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.set_importo(importo)

    def dettagliPagamento(self):
        print(f"Pagamento in contanti di: €{self.get_importo():.2f}")

    def inPezziDa(self):
        importo = self.get_importo()
        pezzi = {
            "banconote da 500 euro": 500,
            "banconote da 200 euro": 200,
            "banconote da 100 euro": 100,
            "banconote da 50 euro": 50,
            "banconote da 20 euro": 20,
            "banconote da 10 euro": 10,
            "banconote da 5 euro": 5,
            "monete da 2 euro": 2,
            "monete da 1 euro": 1,
            "monete da 0.5 euro": 0.5,
            "monete da 0.2 euro": 0.2,
            "monete da 0.1 euro": 0.1,
            "monete da 0.05 euro": 0.05,
            "monete da 0.01 euro": 0.01
        }
        
        print(f"{importo:.2f} euro da pagare in contanti con:")
        for pezzo, valore in pezzi.items():
            if importo >= valore:
                quantita = int(importo // valore)
                importo -= quantita * valore
                print(f"{quantita} {pezzo}")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nome_titolare, data_scadenza, numero_carta):
        super().__init__()
        self.set_importo(importo)
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagliPagamento(self):
        print(f"Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome_titolare}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")
