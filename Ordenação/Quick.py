from Gera_v import gera_v
def troca(vq, a, b):
        temp = vq[a]    
        vq[a] = vq[b]
        vq[b] = temp

def parciona(vq, a, b):
        x = vq[a]
        while a < b:
            while vq[a] < x:
                a += 1
            while vq[b] > x:
                b -= 1
            if a < b:
                troca(vq, a, b)
                if vq[a] == vq[b]:
                      a += 1
        return a 

def quick(vq, a, b):
    if a < b:
        indice_pivo = parciona(vq, a, b)
        quick(vq, a, indice_pivo - 1)
        quick(vq, indice_pivo + 1, b)
    return vq