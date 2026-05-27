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
    

    def pertence(self, v: str):
        return self.pertenceRec(self.__raiz, v)
    
    def pertenceRec(self, no, v: str):

        if no is None:
            return False
        
        elif no.get_info() == v:
            return True
        
        else:
            return self.pertenceRec(no.get_sae(), v) or self.pertenceRec(no.get_sad(), v)
    

    def folhas(self):
        return self.folhasRec(self.__raiz)

    def folhasRec(self, no):

        if no is None:
            return 0
        
        elif no.get_sae() is None and no.get_sad() is None:
            return 1
        
        else: 
            return self.folhasRec(no.get_sae()) + self.folhasRec(no.get_sad())
    

    def numNos(self):
        return self.numNosRec(self.__raiz)
    
    def numNosRec(self, no):
        
        if no is None:
            return 0
        
        else:
            return 1 + self.numNosRec(no.get_sae()) + self.numNosRec(no.get_sad())
    

    def altura(self):
        return self.alturaRec(self.__raiz)
    
    def alturaRec(self, no):

        if no is None:
            return -1
        
        alt_sae =  self.alturaRec(no.get_sae())
        alt_sad = self.alturaRec(no.get_sad())

        if alt_sae >= alt_sad:
            return alt_sae + 1
        
        else:
            return alt_sad + 1
    

    def igual(self, arvore2):
        return self.igualRec(self.__raiz, arvore2.__raiz)
    
    def igualRec(self, no, no2):

        if no is None and no2 is None:
            return True
        
        if no is not None and no2 is not None:

            if no.get_info() == no2.get_info():
                return (self.igualRec(no.get_sae(), no2.get_sae()) 
                        and self.igualRec(no.get_sad(), no2.get_sad()))
            
            else:
                return False
            
        else:
            return False
        
    
    def imprimePre(self):
        return self.imprimePreRec(self.__raiz)
    
    def imprimePreRec(self, no):

        if no is None:
            return "<>"
        
        else:
            result = "<" + no.get_info()
            result = result + self.imprimePreRec(no.get_sae())
            result = result + self.imprimePreRec(no.get_sad())
            result = result + ">"
            return result
        
    
    def imprimeSim(self):
        return self.imprimeSimRec(self.__raiz)
    
    def imprimeSimRec(self, no):

        if no is None:
            return "<>"
        
        else:
            result = "<"
            result = result + self.imprimeSimRec(no.get_sae())
            result = result + no.get_info()
            result = result + self.imprimeSimRec(no.get_sad())
            result = result + ">"
            return result
        
    
    def imprimePos(self):
        return self.imprimePosRec(self.__raiz)
    
    def imprimePosRec(self, no):

        if no is None:
            return "<>"
        
        else:
            result = "<"
            result = result + self.imprimePosRec(no.get_sae())
            result = result + self.imprimePosRec(no.get_sad())
            result = result + no.get_info() 
            result = result + ">"
            return result