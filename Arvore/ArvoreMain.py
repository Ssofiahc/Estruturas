from NoArvore import NoArvore
from Arvore import Arvore

class main:
    
    #ARVORE 1

    #Seleções:
    s1 = NoArvore("Brasil")
    s2 = NoArvore("Argentina")
    s3 = NoArvore("França")
    s4 = NoArvore("Alemanha")

    #Semifinais:
    semi1 = NoArvore("Semifinal 1")
    semi1.set_sae(s1)
    semi1.set_sad(s2)

    semi2 = NoArvore("Semifinal 2")
    semi2.set_sae(s3)
    semi2.set_sad(s4)

    #Final:
    final = NoArvore("Final")
    final.set_sae(semi1)
    final.set_sad(semi2)

    copa = Arvore()
    copa.defineRaiz(final)

    #imprimePre
    print(copa.imprimePre())

    #imprimeSim
    print(copa.imprimeSim())

    #imprimePos
    print(copa.imprimePos())

    #numNos
    print(copa.numNos())

    #folhas:
    print(copa.folhas())

    #altura:
    print(copa.altura())

    #pertence:
    print(copa.pertence("Brasil"))

    #ARVORE 2

    #Seleções:
    s_1 = NoArvore("Brasil")
    s_2 = NoArvore("Argentina")
    s_3 = NoArvore("França")
    s_4 = NoArvore("Alemanha")

    #Semifinais:
    semi_1 = NoArvore("Semifinal 1")
    semi_1.set_sae(s_1)
    semi_1.set_sad(s_2)

    semi_2 = NoArvore("Semifinal 2")
    semi_2.set_sae(s_3)
    semi_2.set_sad(s_4)

    #Final:
    fin = NoArvore("Final")
    fin.set_sae(semi_1)
    fin.set_sad(semi_2)

    cop = Arvore()
    cop.defineRaiz(fin)

    #imprimePre
    print(cop.imprimePre())

    #imprimeSim
    print(cop.imprimeSim())

    #imprimePos
    print(cop.imprimePos())

    #numNos
    print(cop.numNos())

    #folhas:
    print(cop.folhas())

    #altura:
    print(cop.altura())

    #pertence:
    print(cop.pertence("Paraguai"))

    #Teste da igualdade entre as Árvores:
    print(copa.igual(cop))

if __name__ == "__main__":
    main()