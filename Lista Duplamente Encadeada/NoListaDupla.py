class NoListaDupla:
    def __init__(self, info):
        self.__info = info
        self.__prox = None
        self.__ant = None
    
    def set_info(self, info):
        self.__info = info

    def set_prox(self, prox):
        self.__prox = prox
    
    def set_ant(self, ant):
        self.__ant = ant

    def get_info(self):
        return self.__info
    
    def get_prox(self):
        return self.__prox
    
    def get_ant(self):
        return self.__ant