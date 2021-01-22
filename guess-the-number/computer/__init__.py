import random
def guess_computer(x):
    teto = x
    piso = 1
    resposta_user = 0
    while resposta_user != 3:
        chute_computador = random.randint(piso, teto)
        print("O número é : {}".format(chute_computador))
        resposta_user = int(input("Se a alternativa for maior digite 1"
                          ", se for menor digite 2,"
                          "se estiver correta digite 3: "))
        if resposta_user == 1:
            piso = chute_computador
        elif resposta_user == 2:
            teto = chute_computador
        elif resposta_user == 3:
            print(f"A resposta correta era {chute_computador}")
            break
        else:
            resposta_user = int(input(f"O chute foi {chute_computador}. Se o número é MAIOR digite 1, "
                  f"se MENOR digite 2. Se a resposta está correta digite 3!"))

teto = int(input("Coloque o valor máximo: "))
guess_computer(teto)
