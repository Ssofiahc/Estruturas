import random
import sys

def gera_v(tamanho):
    v = random.sample(range(1, sys.maxsize), (tamanho))
    return v