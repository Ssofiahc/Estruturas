from Gera_v import gera_v
from Quick import quick

#execução individual:

tam = int(input("tamanho: "))
v = gera_v(tam)
print("lista embaralhada: ", v)
v = quick(v, 0, len(v) - 1)
print("lista ordenada: ", v)