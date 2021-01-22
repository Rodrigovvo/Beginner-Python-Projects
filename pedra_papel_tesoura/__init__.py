import random
def game():
    escolhas = ['1', '2', '3'] #1 - pedra; 2 -papel; 3-tesoura
    computador = escolhas[random.randint(0, len(escolhas))]
    usuario = input("Digite 1 para Pedra, 2 para Papel e 3 para Tesoura : ")

    vencedor(usuario, computador)


def  vencedor(a, b):
    if a == b:
        print("Empate")
    elif (a == '1' and b == '2') or (a =='2' and b=='3') or (a =='3' and b =='1'):
        print("Você perdeu")
    else:
        print("Você ganhou!!")

game()
