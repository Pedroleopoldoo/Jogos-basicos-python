from random import randint


def jogot():
    def entrada():
        print("-" * 36)
        print("  Bem vindo ao jogo de adivinhação")
        print("-" * 36)


    def pedido():
        print("Dificuldade:")
        print("(1) - fácil   (12 chances)\n(2) - médio   (6 chances)\n(3) - difícil (3 chances)")
        dif = int(input("Qual dificuldade você quer? "))
        return dif


    def diff(dif):
        if dif == 1:
            print("Você escolheu a dificuldade fácil")
            n = 100
        elif dif == 2:
            print("Você escolheu a dificuldade média")
            n = 200
        elif dif == 3:
            print("Você escolheu a dificuldade difícil")
            n = 400
        else:
            print("Você tentou burlar o jogo e por isso só terá uma chance")
            n = 1200
        return n


    def central(di):
        po = 1200
        cont = 1
        while po != 0:
            jogador = int(input("Qual sua escolha? "))
            if jogador < 1 or jogador > 100:
                print("Por favor escolha um número entre 1 e 100")
                continue
            if computador == jogador:
                print(f"Meus parabéns, com o número escolhido de {jogador}, você acertou")
                break
            else:
                po -= di
                if computador > jogador:
                    print("Escolha um número maior")
                    cont += 1
                if computador < jogador:
                    print("Escolha um número menor")
                    cont += 1
        return po


    entrada()
    nome = str(input("Qual seu nome? "))
    dificuldade = pedido()
    chances = diff(dificuldade)
    computador = randint(1, 100)
    pontos = central(chances)

    print(f"{nome} ficou com {pontos} pontos no final do jogo")
    if pontos > 0:
        arquivo = open("lista-de-campeoes.txt", "r")
        conteudo = arquivo.readlines()
        conteudo.append(f"\n{nome:<8} {'-->':^5} {pontos:>5}")
        arquivo = open("lista-de-campeoes.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()


if(__name__ == "__main__"):
    jogot()
