from threading import Semaphore, Thread
from time import sleep

lista_proce = []
processos = [150, 300, 200, 50, 100]
semaphore = Semaphore(1)


def execute_task(ver):
    semaphore.acquire()
    if ver == 1:
        print("\n------------------First-Fit------------------")
        firstfit(processos)
    elif ver == 2:
        print("\n-------------------Best-Fit------------------")
        bestfit(processos)
    else:
        print("\n------------------Worst-Fit------------------")
        worstfit(processos)
    semaphore.release()


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

    print("Escolha o algoritmo de alocação:")
    print("1. First-fit")
    print("2. Best-fit")
    print("3. Worst-fit")
    print("4. Sair")
    ver = int(input())

    numero_p = int(input("Numero de processos: "))
    numero_threads = int(input("Numero de threads: "))
    for _ in range(numero_p):
        while True:
            try:
                valor = int(input(f"Valor do processo {_}: "))
                assert valor > 0
                lista_proce.append(valor)
                break
            except AssertionError:
                print("Tamanho do processo nao pode ser negativo ou nulo! Tente novamente.")

    print("-------------STARTING OPERATION--------------\n")
    for d in range(45):
        sleep(0.1)
        print("-", end='')

    threads = []
    for _ in range(numero_threads):
        thread = Thread(target=execute_task, args=(ver,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Processos antes:", processos)


if __name__ == "__main__":
