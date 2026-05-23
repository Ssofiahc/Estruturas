from Gera_v import gera_v
def mergeS(v, p, r):
    if p < r:
        q = ((p + r)//2)
        mergeS(v, p, q)
        mergeS(v, q + 1, r)
        merge(v, p, q, r)
    return v
            
def merge(vm, p, q, r):
        n1 = q - p + 1
        n2 = r - q

        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)

        for i in range(n1):
            L[i] = vm[p + i]
        for j in  range(n2):
            R[j] = vm[q + j + 1]

        L[n1] = float('inf')
        R[n2] = float('inf')

        i = 0
        j = 0

        for k in range(p, r + 1):
            if L[i] <= R[j]:
                vm[k] = L[i]
                i += 1
            else:
                vm[k] = R[j]
                j += 1