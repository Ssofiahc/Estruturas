from abc import ABC, abstractmethod

class Fila(ABC):

    @abstractmethod
    def enqueue(self, v: int):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def reset(self):
        pass