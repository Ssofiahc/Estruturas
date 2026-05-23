class NoLista:
    
    def __init__(self, info):
        self.__info = info
        self.__prox = None

    def set_info(self, info):
        self.__info = info
        
    def get_info(self):
        return self.__info
    
    def set_prox(self, prox):
        self.__prox = prox

    def get_prox(self):
        return self.__prox
    
    def __str__(self):
        return str(self.get_info())