from ListaDupla import ListaDupla

def MainDupla():

    print("uso do método Lista():")
    lista = ListaDupla()

    #vazia
    print("uso do método vazia():")
    print("lista vazia", lista.vazia())

    #insere valores
    print("uso do método insere()")
    lista.insere("a")
    lista.insere("b")
    lista.insere("c")
    lista.insere("d")
    lista.insere("e")
    lista.insere("f")

    #imprime
    print("uso do método imprime():")
    lista.imprime()

    #comprimento
    print("uso do método comprimento():")
    print("comprimento lista: ", lista.comprimento())
    
    #busca
    print("uso do método busca():")
    v = "c"
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
    v = "b"
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

    #insere_fim
    print("uso do método insere_fim():")
    v = "h"
    lista.insere_fim(v)

    #imprime_numerada
    print("uso do método imprime_numerada():")
    lista.imprime_numerada()

    
if __name__ == "__main__":
    MainDupla()