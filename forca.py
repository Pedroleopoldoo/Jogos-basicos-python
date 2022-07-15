import random

principal = []


def jogof():
    def inicio():
        print("-" * 30)
        print("  Bem vindo ao jogo da forca")
        print("-" * 30)

    def pedido():
        print("Dificuldade:")
        print("(1) - fácil   (6 chances)\n(2) - médio   (4 chances)\n(3) - difícil (2 chances)")
        dif = int(input("Qual dificuldade você quer? "))
        return dif

    def diff(dif):
        if dif == 1:
            print("Você escolheu a dificuldade fácil")
            n = 200
        elif dif == 2:
            print("Você escolheu a dificuldade média")
            n = 300
        elif dif == 3:
            print("Você escolheu a dificuldade difícil")
            n = 600
        else:
            print("Você tentou burlar o jogo e por isso só terá uma chance")
            n = 1200
        return n

    def central(esc):
        po = 1200
        for letra in escolha:
            principal.append("_")
        acertou = False
        while po != 0 and not acertou:
            tentativa = str(input("Me diga uma letra: ")).lower().strip()[0]
            if tentativa in esc and tentativa not in principal:
                cont = 0
                for letra in esc:
                    if tentativa == letra:
                        principal[cont] = letra
                    cont += 1
                print(principal)
            else:
                po -= chances
                print("Essa letra não pertence à palavra")
            acertou = "_" not in principal
        return po

    inicio()
    nome = str(input("Qual seu nome? "))
    dificuldade = pedido()
    chances = diff(dificuldade)
    escolha = str(input("Mestre do jogo, diga a palavra secreta: ")).lower().strip()
    pontos = central(escolha)
    print(f"{nome} ficou com {pontos} pontos, volte sempre")
    if pontos > 0:
        arquivo = open("lista-de-campeoes.txt", "r")
        conteudo = arquivo.readlines()
        conteudo.append(f"\n{nome:<8} {'-->':^5} {pontos:>5}")
        arquivo = open("lista-de-campeoes.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()


if(__name__ == "__main__"):
    jogof()
