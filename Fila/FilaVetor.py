from Fila import Fila

class FilaVetor(Fila):
    def __init__(self, tam):
        self.__tam = tam
        self.__n = 0
        self.__ini = 0
        self.__vet = [0]*tam

    def get_tam(self):
        return self.__tam

    def get_n(self):
        return self.__n

    def get_ini(self):
        return self.__ini
    
    def get_vet(self):
        return self.__vet

    def enqueue(self, v: int):
        
        if self.__n == self.__tam:
            print("Fila cheia.")
            return
        
        fim = (self.__ini + self.__n) % self.__tam
        self.__vet[fim] = v
        self.__n += 1
        
        return
    
    def dequeue(self):
        
        if self.__n == 0:
            raise IndexError("ERRO! Fila vazia!")
        
        else:
            v = self.__vet[self.__ini]
            self.__ini = (self.__ini + 1) % self.__tam
            self.__n -= 1
            return v
    
    def isEmpty(self):
        
        if self.__n == 0:
            return True
        
        else:
            return False
    
    def reset(self):

        self.__n = 0
        self.__ini = 0
        
        return
    
    def toString(self):

        if self.isEmpty():
            print("Fila vazia!")
            return
        
        elem = []
        v = self.__ini

        for _ in range(self.__n):
            elem.append(str(self.__vet[v]))
            v = (v + 1) % self.__tam

        filaPrint = "Fila: " + ", ".join(elem)
        print(filaPrint)
        return filaPrint
    
    def concatena(self, f2):

        tam_conc = self.__tam + f2.get_tam()
        fila_conc = FilaVetor(tam_conc)
        v1 = self.__ini

        for _ in range(self.__n):
            fila_conc.enqueue(self.__vet[v1])
            v1 = (v1 + 1) % self.__tam

        v2 = f2.get_ini()

        for _ in range(f2.get_n()):
            fila_conc.enqueue(f2.get_vet()[v2])
            v2 = (v2 + 1) % f2.get_tam()

        return fila_conc
    
    def merge(self, f2):

        tam_conc = self.__tam + f2.get_tam()
        fila_conc = FilaVetor(tam_conc)
        v1 = self.__ini
        v2 = f2.get_ini()
        cont1 = 0
        cont2 = 0

        while cont1 < self.__n or cont2 < f2.get_n():

            if cont1 < self.__n:
                fila_conc.enqueue(self.__vet[v1])
                v1 = (v1 + 1) % self.__tam
                cont1 += 1

            if cont2 < f2.get_n():
                fila_conc.enqueue(f2.get_vet()[v2])
                v2 = (v2 + 1) % f2.get_tam()
                cont2 += 1

        return fila_conc