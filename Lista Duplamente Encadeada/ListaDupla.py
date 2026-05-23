from NoListaDupla import NoListaDupla

class ListaDupla:
    def __init__(self):
        self.__prim = None

    def insere(self, v: str):
        novo = NoListaDupla(v)
        novo.set_prox(self.__prim)
        novo.set_ant(None)

        if self.__prim is not None:
            self.__prim.set_ant(novo)

        self.__prim = novo

    def imprime(self):
        p = self.__prim
        while p:
            print(f"Nó: {p.get_info()}")
            p = p.get_prox()
    
    def vazia(self):
            if self.__prim is None:
                return True
            else:
                return False
    
    def busca(self, v: str):
        p = self.__prim
        while p is not None:
            if p.get_info() == v:
                return p
            p = p.get_prox()
        return None
    
    def comprimento(self):
        p = self.__prim
        cont = 0
        while p is not None:
            cont += 1
            p = p.get_prox()     
        return cont
    
    def ultimo(self):
        if self.__prim is None:
            return None
        p = self.__prim
        while p.get_prox() is not None:
            p = p.get_prox()
        return p
    
    def retira(self, v: str):
        p = self.busca(v)
        if p is None:
            return
        if self.__prim is p:
            self.__prim = p.get_prox()
        else:
            p.get_ant().set_prox(p.get_prox())
        if p.get_prox() is not None:
            p.get_prox().set_ant(p.get_ant())

    def libera(self):
        self.__prim = None

    def insere_fim(self, v: str):
        novo = NoListaDupla(v)
        if self.vazia():
            self.__prim = novo
        else:
            ult = self.ultimo()
            ult.set_prox(novo)
            novo.set_ant(ult)

    def insere_meio(self, v: str, pos: int):
        
        if self.vazia() or pos <= 0:
            self.insere(v)
            return
        
        if pos >= self.comprimento():
            self.insere_fim(v)
            return
        
        novo = NoListaDupla(v)
        p = self.__prim
        cont = 0

        while cont < pos:
            p = p.get_prox()
            cont += 1

        anterior = p.get_ant()
        novo.set_prox(p)
        novo.set_ant(anterior)

        anterior.set_prox(novo)
        p.set_ant(novo)

    def mover(self, v: str, pos: int):
        if self.busca(v) is None:
            return print("Música não encontrada na playlist")
        self.retira(v)
        self.insere_meio(v, pos)

    def imprime_numerada(self):
        p = self.__prim
        cont = 1
        while p:
            print(f"{cont}.{p.get_info()}")
            p = p.get_prox()
            cont += 1
    
    def retira_numero(self, pos: int):
        if self.vazia() or pos >= self.comprimento():
            return print("Não foi possível realizar a ação!")        
        cont = 0
        p = self.__prim
        while cont < pos:
            p = p.get_prox()
            cont += 1
        if self.__prim is p:
            self.__prim = p.get_prox()
        else:
            p.get_ant().set_prox(p.get_prox())
        if p.get_prox() is not None:
            p.get_prox().set_ant(p.get_ant())