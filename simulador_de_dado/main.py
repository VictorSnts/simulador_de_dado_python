import random


def jogar_dado():
    msg = 'Gostaria de jogar o dado? Sim ou Não? '

    while valida_resposta(str(input(msg))):
        desenha_dado(random.randint(1, 6))
        msg = '\nGostaria de jogar novamente? Sim ou Não? '

    print("\nAte a proxima...")


def valida_resposta(resposta) -> bool:
    resposta = resposta.lower().replace("ã", "a")

    while not (resposta == "sim" or resposta == "nao"):
        resposta = str(input('\nInforme uma resposta valida: Sim ou Não ')).lower().replace("ã", "a")

    if resposta == "sim":
        return True
    elif resposta == "nao":
        return False


def desenha_dado(nro):
    if nro == 1:
        print("-------")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("-------")
    elif nro == 2:
        print("-------")
        print("| 0   |")
        print("|     |")
        print("|   0 |")
        print("-------")
    elif nro == 3:
        print("-------")
        print("| 0   |")
        print("|  0  |")
        print("|   0 |")
        print("-------")
    elif nro == 4:
        print("-------")
        print("| 0 0 |")
        print("|     |")
        print("| 0 0 |")
        print("-------")
    elif nro == 5:
        print("-------")
        print("| 0 0 |")
        print("|  0  |")
        print("| 0 0 |")
        print("-------")
    elif nro == 6:
        print("-------")
        print("| 0 0 |")
        print("| 0 0 |")
        print("| 0 0 |")
        print("-------")


jogar_dado()
