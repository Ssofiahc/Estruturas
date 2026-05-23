from NoArvore import NoArvore
class Arvore:
    def __init__(self):
        self.__raiz = None
    
    def defineRaiz(self, r):
        self.__raiz = r
    
    def vazia(self):
        if self.__raiz is None:
            return True
        else:
            return False
    
    def pertenceR(self, v: str):
        return self.pertence(self.__raiz, v)
    
    def pertence(self, v: str):
        if self.__raiz is None:
            return False
        elif self.get_info() == v:
            return True
        else:
            return self.pertence(self.get_sae(), v) or self.pertence(self.get_sad(), v)
    
    