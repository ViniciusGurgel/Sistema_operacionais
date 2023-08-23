# Problema 4: "Crie um programa que simule o funcionamento de semáforos num ambiente multitarefa. As threads devem compartilhar recursos e utilizar semáforos para controlar o acesso a esses recursos de forma segura."
from threading import Semaphore, Thread
from time import sleep

memoria_total = 10
contador = 0
semaphore = Semaphore(1)

def execute_task():
    global memoria_total
    global contador

    for _ in range(5):
        semaphore.acquire()
        if memoria_total > 0:
            print(f"\n\n\t================OPERATING AT PROCESS TREE:============= =>: {contador}MB/s\n")
            sleep(1)
            memoria_total -= 1
            contador += 1
        semaphore.release()

print("\t\t-------------STARTING OPERATION--------------\n")
c = 10
for d in range(c):
    sleep(0.5)
    print("\t-", end='')

threads = []
num_threads = 3

for _ in range(num_threads):
    thread = Thread(target=execute_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

if memoria_total == 0:
        print(
            "\n===============================QUANTIDADE DE MEMORIA TOTAL OCUPADA. O SISTEMA IRÁ PARAR AS EXECUÇÕES PARA EVITAR UM DEADLOCK!==============================\n")
        resposta = input("DESEJA INTERROMPER AS EXECUÇÕES? (Yes/No): ")
        if resposta.lower() == 'yes':
            print("\t\t------------SYSTEM INTERRUPTED----------\n")
        else:
            print("\t\t============= [FATAL ERROR] UNEXPECTED CATASTROPHIC FAILURE!!=============\n")
