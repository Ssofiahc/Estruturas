from FilaVetor import FilaVetor
class FilaMain:
    @staticmethod
    def teste():

        fila = FilaVetor(10)
        fila2 = FilaVetor(5)

        #Teste de isEmpty nas duas filas:
        
        if fila.isEmpty():
            print("Fila 1 vazia!")
        else:
            print("Fila 1 não está vazia!")

        if fila2.isEmpty():
            print("Fila 2 vazia!")
        else:
            print("Fila 2 não está vazia!")

        #Teste de enqueue nas duas filas:

        fila.enqueue(1)
        fila.enqueue(2)
        fila.enqueue(3)
        fila.enqueue(4)
        fila.enqueue(5)

        #Teste de toString em fila:
        fila.toString()
        

        fila2.enqueue(6)
        fila2.enqueue(7)
        fila2.enqueue(8)
        fila2.enqueue(9)
        fila2.enqueue(10)
        
        #teste de toString em fila2:

        fila2.toString()

        #Teste de dequeue nas duas filas:

        fila.dequeue()
        fila.dequeue()

        fila2.dequeue()
        fila2.dequeue()

        #Teste de toString nas duas filas:

        fila.toString()
        fila2.toString()

        #Teste de concatena:

        filaConcatena = fila.concatena(fila2)
        filaConcatena.toString()

        #Teste de merge:

        filaMerge = fila.merge(fila2)
        filaMerge.toString()

        #Teste de reset:

        fila.reset()
        fila2.reset()
    
    def cliente():

        tam = int(input("Capacidade máxima da fila: "))
        filaAtendimento = FilaVetor(tam)

        print("""
              Operações:
              1. Nova senha
              2. Chamar senha
              3. Exibir fila atual
              4. Reiniciar atendimento
              5. Encerrar
              """)

        senha = 1

        while True:

            x = int(input("Qual operação deseja realizar? "))

            if x == 1:

                if filaAtendimento.get_n() < filaAtendimento.get_tam():
                    filaAtendimento.enqueue(senha)
                    print(f"Senha {senha} inserida na fila!")
                    senha = senha + 1

                else:
                    print("Fila cheia! Aguarde.")

            elif x == 2:

                if not filaAtendimento.isEmpty():
                    chama = filaAtendimento.get_ini()
                    filaAtendimento.dequeue()
                    print(f"Chamando {chama}")

                else:
                    print("Fila vazia")

            elif x == 3:

                if filaAtendimento.isEmpty():
                    print("Fila vazia!")

                else:
                    print("Fila atual:")
                    filaAtendimento.toString()
            
            elif x == 4:
                
                filaAtendimento.reset()
                print("Fila reiniciada!")
            
            elif x == 5:
                break

            else:
                raise IndexError("Opção indisponível.")

if __name__ == "__main__":
    FilaMain.teste()
    FilaMain.cliente()