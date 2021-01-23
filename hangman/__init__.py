# Famosa forca
import random
import string

from palavras import palavras


def escolhendo_uma_palavra(palavras):
    return random.choice(palavras).upper()


def inicio_jogo_forca():
    palavra_esolhida = escolhendo_uma_palavra(palavras)
    letras = set(palavra_esolhida)
    alfabeto = set(string.ascii_uppercase)
    letras_tentadas = set()
    print("============================================")
    print("==============NOVO=JOGO=====================")
    print("============================================")
    print(f"A palavra escolhida tem {len(palavra_esolhida)} letras !!")

    while len(letras) > 0:
        print("")
        tentativa = input("Chute uma letra: ").upper()

        if tentativa in alfabeto - letras_tentadas:
            letras_tentadas.add(tentativa)
            if tentativa in letras:
                print(f"Parabéns! A palavra contém {tentativa}")
                letras.remove(tentativa)
                print(f"Faltam {len(letras)} letras.")
            else:
                print(f"A palavra não contém a letra {tentativa}")
            for i in palavra_esolhida:
                if i not in letras_tentadas:
                    print(" _ ", end="")
                else:
                    print(" " + i, end=" ")

        else:
            print("A letra informada já foi utilizada, tente novamente! ")
    print(f"Conseguiu !!! A palavra escolhida era {palavra_esolhida}")


inicio_jogo_forca()
