from Gera_v import gera_v
from Merge import mergeS

#execução individual:

tam = int(input("tamanho: "))
v = gera_v(tam)
print("lista embaralhada: ", v)
v = mergeS(v, 0, len(v) - 1)
print("lista ordenada: ", v)