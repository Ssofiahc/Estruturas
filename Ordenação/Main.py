import time
from Gera_v import gera_v
from Bubble import bubble
from Quick import quick
from Merge import mergeS

#Gera a lista v

tam = int(input("tamanho da lista: "))

v = gera_v(tam)

print("lista embaralhada: ", v)

#copia lista v para que possa ser utilizada individualmente para cada algoritmo

vb = v.copy()
vq = v.copy()
vm = v.copy()

#ordena as cópias e contabiliza o tempo de cada algoritmo

inicio_b = time.time()
vb = bubble(vb)
fim_b = time.time()
delta_b = (fim_b) - (inicio_b)

inicio_q = time.time()
vq = quick(vq, 0, len(vq) - 1)
fim_q = time.time()
delta_q = fim_q - inicio_q

inicio_m = time.time()
vm = mergeS(vm, 0, len(vm) - 1)
fim_m = time.time()
delta_m = fim_m - inicio_m

print(f"lista ordenada: {vq}")
print(f"tempo bubble sort: {delta_b:.6f}")
print(f"tempo quick sort: {delta_q:.6f}")
print(f"tempo merge sort: {delta_m:.6f}")

#verificação

if vb == vq == vm:
    print("Sucesso.")
else:
    print("Erro.")