class NoArvore:
    def __init__(self, info):
        self.__info = info
        self.__sae = None
        self.__sad = None
        
    def set_info(self, info):
        self.__info = info
    
    def set_sae(self, sae):
        self.__sae = sae
    
    def set_sad(self, sad):
        self.__sad = sad

    def get_info(self):
        return self.__info
    
    def get_sae(self):
        return self.__sae
    
    def get_sad(self):
        return self.__sad