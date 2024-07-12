from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave):
        self.chiave = chiave

    def _sposta_carattere(self, c, chiave):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + chiave) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + chiave) % 26 + ord('A'))
        else:
            return c

    def codifica(self, testoInChiaro):
        return ''.join(self._sposta_carattere(c, self.chiave) for c in testoInChiaro)

    def _decodifica_carattere(self, c, chiave):
        return self._sposta_carattere(c, -chiave)

    def decodifica(self, testoCodificato):
        return ''.join(self._decodifica_carattere(c, self.chiave) for c in testoCodificato)

    def leggi_da_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def scrivi_su_file(self, testo, file_path):
        with open(file_path, 'w') as file:
            file.write(testo)

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n):
        self.n = n

    def _combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        parte1 = testo[:metà]
        parte2 = testo[metà:]
        combinato = ''.join(p1 + p2 for p1, p2 in zip(parte1, parte2))
        if len(parte1) > len(parte2):
            combinato += parte1[-1]
        return combinato

    def codifica(self, testoInChiaro):
        for _ in range(self.n):
            testoInChiaro = self._combinazione(testoInChiaro)
        return testoInChiaro

    def _decodifica_combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        parte1 = testo[:metà]
        parte2 = testo[metà:]
        decodificato = []
        for i in range(len(parte2)):
            decodificato.append(parte1[i])
            decodificato.append(parte2[i])
        if len(parte1) > len(parte2):
            decodificato.append(parte1[-1])
        return ''.join(decodificato)

    def decodifica(self, testoCodificato):
        for _ in range(self.n):
            testoCodificato = self._decodifica_combinazione(testoCodificato)
        return testoCodificato

    def leggi_da_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def scrivi_su_file(self, testo, file_path):
        with open(file_path, 'w') as file:
            file.write(testo)



cifratore = CifratoreAScorrimento(3)
testo_codificato = cifratore.codifica("abc")
print(testo_codificato)
testo_decodificato = cifratore.decodifica(testo_codificato)
print(testo_decodificato)

combinatore = CifratoreACombinazione(1)
testo_codificato = combinatore.codifica("abcdefghi")
print(testo_codificato)
testo_decodificato = combinatore.decodifica(testo_codificato)
print(testo_decodificato)
