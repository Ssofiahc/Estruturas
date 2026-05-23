from Gera_v import gera_v
from Bubble import bubble

#execução individual:

tam = int(input("tamanho: "))
v = gera_v(tam)
print("lista embaralhada: ", v)
v = bubble(v)
print("lista ordenada: ", v)