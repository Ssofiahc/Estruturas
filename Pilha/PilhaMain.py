from Pilha import Pilha
from Calc import Calc
def PilhaMain():

    #Teste da pilha:

    pilha = Pilha()  

    #vazia()
    pilha.vazia()

    #pop()
    pilha.pop()  

    #push()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(9)

    #pop()
    pilha.pop()
    
    #vazia()
    pilha.vazia()

    #top()
    pilha.top()

    #libera()
    pilha.libera()

    #vazia()
    pilha.vazia()

    if pilha.vazia() is True:
        print("Pilha liberada!")

    #Calculadora:
    calculadora = Calc(".2f")

    print("""Operações:
          1. Inserir expressão
          2. Encerrar calculadora
          3. Limpar calculadora""")
    
    while True:

        opr = int(input("Operação escolhida: "))

        if opr == 1:
            expr = str(input("Insira a expressão: "))
            calculadora.interpreta(expr)

        elif opr == 2:
            print("Calculadora encerrada!")
            break

        elif opr == 3:
            calculadora.libera()
            
        else:
            print("Erro. Operação inexistente!")


if __name__ == "__main__":
    PilhaMain()