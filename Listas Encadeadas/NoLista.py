class NoLista:
    
    def __init__(self, info):
        self.info = info
        self.prox = None

    def set_info(self, info):
        self.info = info
        
    def get_info(self):
        return self.info
    
    def set_prox(self, prox):
        self.prox = prox

    def get_prox(self):
        return self.prox
    
    def __str__(self):
        return str(self.get_info())