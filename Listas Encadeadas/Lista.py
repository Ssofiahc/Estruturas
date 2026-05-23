from NoLista import NoLista
class Lista:    

    def __init__(self):
        self.prim = None
    
    def insere (self, info: int):
        novo = NoLista(info)
        novo.prox = self.prim
        self.prim = novo

    def imprime(self):
        p = self.prim
        while p:
            print(f"Nó: {p.get_info()}")
            p = p.prox
    
    def __str__(self):
        elementos = []
        p = self.prim

        while p is not None:
            elementos.append(str(p.get_info()))
            p = p.prox
        return " ".join(elementos) if elementos else "Lista vazia."
    
    def vazia(self):
        if self.prim is None:
            return True
        else:
            return False
    
    def busca(self, v: int):
        p = self.prim
        while p is not None:
            if p.info == v:
                return p
            p = p.prox
        return None
    
    def comprimento(self):
        p = self.prim
        cont = 0
        while p is not None:
            cont += 1
            p = p.prox     
        return cont
    
    def ultimo(self):
        if self.prim is None:
            return None
        p = self.prim
        while p.prox is not None:
            p = p.prox
        return p

    def libera(self):
        self.prim = None

#Lista 3

    def retira(self, v: int):
        ant = None
        p = self.prim
        while (p is not None) and (p.get_info() != v):
            ant = p
            p = p.prox
        if p is None:
            return
        if ant is None:
            self.prim = p.prox
        else:
            ant.prox = p.prox

    def insere_fim(self, info: int):
        novo = NoLista(info)
        if self.vazia():
            self.prim = novo
        else:
            ult = self.ultimo()
            ult.prox = novo
    
    def igual(self, L2):
        p1 = self.prim
        p2 = L2.prim
        while p1 is not None and p2 is not None:
            if p1.get_info() != p2.get_info():
                return False
            p1 = p1.prox
            p2 = p2.prox
        
        if p1 == p2:
            return True
        else:
            return False
    
    def imprimeRecursivo(self):
        self.__imprimeRecursivoAux(self.prim)
    
    def __imprimeRecursivoAux(self, l):
        if l is not None:
            print(l.get_info())
            self.__imprimeRecursivoAux(l.prox)
    
    def retiraRecursivo(self, v: int):
        self.prim = self.__retiraRecursivoAux(self.prim, v)
    
    def __retiraRecursivoAux(self, l, v: int):
        if l is not None:
            if l.get_info() == v:
                l = l.prox
            else:
                l.prox = self.__retiraRecursivoAux(l.prox, v)
        return l
    
    def igualRecursivo(self, l):
        return self.__igualRecursivoAux(self.prim, l.prim)
    
    def __igualRecursivoAux(self, l1, l2):
        if (l1 == None) and (l2 == None):
            return True
        else:
            if l1 is None or l2 is None:
                return False
            else:
                return ((l1.get_info() == l2.get_info()) and self.__igualRecursivoAux(l1.prox, l2.prox))
    
    def comprimentoRecursivo(self):
        return self.__comprimentoRecursivoAux(self.prim)
    
    def __comprimentoRecursivoAux(self, l):
        if l is None:
            return 0
        else:
            return 1 + self.__comprimentoRecursivoAux(l.prox)
    
#Extra

    def insereOrdenado(self, v: int):

        ant = None
        p = self.prim

        while p is not None and p.get_info() < v:
            p = ant
            p.get_prox()

        novo = NoLista(v)

        if ant == None:
            novo.prox = self.prim
            self.prim = novo

        else:
            novo.prox = ant.prox
            ant.prox = novo