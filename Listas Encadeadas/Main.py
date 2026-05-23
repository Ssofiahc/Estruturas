from Lista import Lista

def Main():

    print("uso do método Lista():")
    lista = Lista()
    lista2 = Lista()

    #vazia
    print("uso do método vazia():")
    print("lista vazia", lista.vazia())
    print("lista2 vazia", lista.vazia())

    #insere valores
    print("uso do método insere()")
    lista.insere(5)
    lista.insere(4)
    lista.insere(3)
    lista.insere(2)
    lista.insere(1)
    lista.insere(0)

    lista2.insere(0)
    lista2.insere(1)
    lista2.insere(2)
    lista2.insere(3)
    lista2.insere(4)
    lista2.insere(5)

    #imprime
    print("uso do método imprime():")
    lista.imprime()
    lista2.imprime()

    #comprimento
    print("uso do método comprimento():")
    print("comprimento lista: ", lista.comprimento())
    
    #busca
    print("uso do método busca():")
    v = 3
    busc = lista.busca(v)
    if busc:
        print("Achou em: ", busc)

    #ultimo
    print("uso do método ultimo():")
    ult = lista.ultimo()
    if ult:
        print("O último nó contém: ", ult)
    
    #retira
    print("uso do método retira():")
    v = 5
    lista.retira(v)

    #mostra lista atual
    print("uso do método imprime():")
    lista.imprime()

    #libera
    print("uso do método libera():")
    lista.libera()

    #mostra lista atual
    print("uso do método vazia():")
    if lista.vazia():
        print("lista liberada.")

#LISTA 3:

    #insere_fim
    print("uso do método insere_fim():")
    v = 6
    lista2.insere_fim(v)

    #imprimeRecursivo
    print("uso do método imprimeRecursivo():")
    print("lista2 atualizada: ") 
    lista2.imprimeRecursivo()

    #igual
    print("uso do método igual():")
    print("Testando a igualdade: ", lista.igual(lista2))

    #retiraRecursivo
    print("uso do método retiraRecursivo():")
    v2 = 4
    lista2.retiraRecursivo(v2)

    #imprimeRecursivo
    print("uso do método imprimeRecursivo():")
    print("lista2 atualizada: ")
    lista2.imprimeRecursivo()

    #igualRecursivo
    print("uso do método igualRecursivo():")
    print("lista:")
    lista.imprimeRecursivo()
    print("lista2:")
    lista2.imprimeRecursivo()
    if lista.igualRecursivo(lista2):
        print("são iguais!")
    else:
        print("são diferentes!")

    #comprimentoRecursivo
    print("uso do método insereRecursivo():")
    print("comprimento lista2: ", lista2.comprimentoRecursivo())

if __name__ == "__main__":
    Main()