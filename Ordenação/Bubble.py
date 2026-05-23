from Gera_v import gera_v

def bubble(v):
    
    n = len(v)
   
    for i in range(n-1,0,-1):

        troca = False

        for j in range(0, i):

            if v[j] > v[j + 1]:

                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
                troca = True
                
        if not troca:
            break
        
    return v