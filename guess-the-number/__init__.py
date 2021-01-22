import random
def guess(x):
    numero_aleatorio = random.randint(1, x)
    guess = int(input("Chute um número: "))
    while ( guess != numero_aleatorio) :
        if guess > numero_aleatorio:
            print("O chute foi muito alto")
            chute = int(input("Tente outro número: "))
            guess = chute
        else:
            print("O chute foi muito baixo")
            chute = int(input("Tente outro número: "))
            guess = chute
    print("Parabéns acertou! O número selecionado era: {}".format(numero_aleatorio))



print("======================")
print("++++++BEM-VINDO+++++++")
print("======================")

print("Primeiro Digite o valor máximo e depois tente acertar o número escolhido")
escolha = input("Digite um valor máximo ")
if (escolha.isnumeric()):
    guess(int(escolha))
else:
    input("Digite um valor máximo ")


