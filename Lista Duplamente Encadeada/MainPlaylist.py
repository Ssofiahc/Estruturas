from ListaDupla import ListaDupla

def MainPlaylist():

    lista = ListaDupla()

    lista.insere_meio("Messege in a bottle", 0)
    lista.insere_meio("B.Y.O.B", 1)
    lista.insere_meio("Call me", 2)
    lista.insere_meio("No more tears", 3)
    lista.insere_meio("Freack on a leash", 4)
    lista.insere_meio("Question!", 5)
    
    while True:

        print("""OPERAÇÕES:
                1.Inserir música na playlist
                2.Remover música da playlist
                3.Mover música
                4.Visualizar playlist
                5.Sair
            """)
        
        x = int(input("Qual operação você deseja realizar? "))
        
        if x == 1:

            musica = str(input("Qual música você deseja inserir? "))
            pos = int(input("Em qual posição a música deve ser colocada? "))

            lista.insere_meio(musica, (pos - 1))

            print("Música foi inserida com sucesso! :) ")

        elif x == 2:

            x = int(input("Remover por nome ou posição? (0 ou 1) "))

            if x == 0:
                musica = str(input("Qual música deve ser removida? "))
                lista.retira(musica)
                return print("Música removida com sucesso! :)")
            
            if x == 1:
                musica = int(input("Qual a posição da musica a ser retirada? "))
                lista.retira_numero(musica)
                return print("Música removida com sucesso! :)")
            
            else:
                return print("Inválido!")
        
        elif x == 3:

            musica = str(input("Qual música deve ser movida? "))
            pos = int(input("Para qual posição a música deve ser movida? "))

            lista.mover(musica, (pos - 1))

        elif x == 4:

            print("Sua playlist:")
            lista.imprime_numerada()

        elif x == 5:
            break
        
if  __name__ == "__main__":
    MainPlaylist()