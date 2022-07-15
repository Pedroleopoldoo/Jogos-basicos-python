def apresentação():
    print("-" * 31)
    print("  Bem vindos ao Penguin games")
    print("-" * 31)
    print(f"""Escolhas de jogo para você:
[ 1 ] advinhação
[ 2 ] forca
    """)
    es = int(input("Qual você escolhe? "))
    return es


def jogos(es):
    import advinhação
    import forca
    if es == 1:
        advinhação.jogot()
    elif es == 2:
        forca.jogof()
    else:
        print("ERRO, você não escolheu nenhum jogo")


def campeoes():
    print("\nAtual lista de campeões: ")
    print("-" * 30)
    with open("lista-de-campeoes.txt") as arquivo:
        for linha in arquivo:
            print(f"{linha}")
    print("-" * 30)


escolha = apresentação()
jogos(escolha)
campeoes()
