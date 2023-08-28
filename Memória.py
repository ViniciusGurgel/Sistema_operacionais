import random

lista_proce = []
# processos = [_ * 50 for _ in range(random.randint(2,4),random.randint(5, 7))]
processos = [150, 300, 200, 50, 100]


def firstfit(processos_c):
    global lista_proce

    for tamanho in lista_proce:
        alocado = False

        for _, processo in enumerate(processos_c):
            if processo >= tamanho:
                processos_c[_] -= tamanho
                print(f"Arquivo tamanho {tamanho} alocado na partição {_}.")
                alocado = True
                break

        if not alocado:
            print(f"Arquivo tamanho {tamanho} não pude ser alocado.")
    print(processos_c)


def bestfit(processos_c):
    global lista_proce

    for tamanho in lista_proce:
        alocado = False
        particao = None

        for _, processo in enumerate(processos_c):
            if processo >= tamanho:
                if particao is None or processo < processos_c[particao]:
                    particao = _

        if particao is not None:
            processos_c[particao] -= tamanho
            print(f"Arquivo tamanho {tamanho} alocado na partição {particao}.")
            alocado = True

        if not alocado:
            print(f"Arquivo tamanho {tamanho} não pude ser alocado.")
    print(processos_c)


def worstfit(processos_c):
    global lista_proce

    for tamanho in lista_proce:
        alocado = False
        particao = None

        for _, processo in enumerate(processos_c):
            if processo >= tamanho:
                if particao is None or processo > processos_c[particao]:
                    particao = _

        if particao is not None:
            processos_c[particao] -= tamanho
            print(f"Arquivo tamanho {tamanho} alocado na partição {particao}.")
            alocado = True

        if not alocado:
            print(f"Arquivo tamanho {tamanho} não pude ser alocado.")
    print(processos_c)


def main():
    global lista_proce
    global processos

    numero_p = int(input("Numero de processos: "))
    for _ in range(numero_p):
        valor = int(input(f"Valor do processo {_}: "))
        lista_proce.append(valor)

    print("Processos antes:", processos)

    print("----------------First-Fit----------------")
    firstfit(processos.copy())

    print("-----------------Best-Fit----------------")
    bestfit(processos.copy())

    print("----------------Worst-Fit----------------")
    worstfit(processos.copy())


if __name__ == "__main__":
    main()
