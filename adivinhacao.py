def jogar():

    print("*--------------------------------*")
    print("*----- JOGO DE ADIVINHAÇÃO ------*")
    print("*--------------------------------*")

    from random import randint

    numero_secreto = randint(0,100)
    rodada = 1
    pontos = 1000

    ## ADICIONA NIVEL
    print("Qual nível de dificuldade?")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    nivel = int(input("Defina o nível: "))
    print("")
    print("")

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 8
    elif (nivel == 3):
        total_de_tentativas = 3

    while(rodada <= total_de_tentativas):
        print("Tentativas: ", rodada, "de", total_de_tentativas)
        chute_str = input("Digite um numero entre 0 a 100: ")
        #print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute == numero_secreto):
            print("Você acertou!!", end="\n")
            break
        else:
            if (chute > numero_secreto):
                print("Você errou!! O seu chute foi maior do que o número!", end="\n")
            elif (chute < numero_secreto):
                print("Você errou!! O seu chute foi menor do que o número!", end="\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Quantidade de pontos: ", pontos)
        print("")
        rodada = rodada + 1

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()