from NoLista import NoLista
class Pilha:
    def __init__(self):

        self.__topo = None
    
    def push(self, v: float):

        novo = NoLista(v)
        novo.set_prox(self.__topo)
        self.__topo = novo

    def pop(self):

        if self.__topo is not None:
            v = self.__topo
            removido = v.get_info()
            self.__topo = self.__topo.get_prox()
            return removido
        
        else:
            return 
    
    def vazia(self):

        if self.__topo is None:
            return True
        
        else:
            return False
    
    def top(self):

        if not self.vazia():
            return self.__topo.get_info()
        
        else:
            return
    
    def libera(self):

        self.__topo = None