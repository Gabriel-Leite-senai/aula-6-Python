#lista de tarefas#

tarefas = [
    {"titulo":"estudar","concluida":True,"prioridade":"alta"},
    {"titulo":"comer","concluida":False,"prioridade":"baixa"},
    {"titulo":"ler","concluida":False,"prioridade":"baixa"}
]

def mostar_tarefa(tarefa):
    if tarefa["concluida"]:
        print("[X]", end=" ")
    else:
        print("[ ]", end=" ")
    print(tarefa["titulo"], end=" | ")
    print(tarefa["prioridade"],end="\n")

def mostrar_todas_tarefas():
    for x in tarefas:
        mostar_tarefa(x)

def mostrar_tarefas_concluidas():
    for x in tarefas:
        if x["concluida"]:
            mostar_tarefa(x)

def mostrar_tarefas_pendentes():
    for x in tarefas:
        if not x["concluida"]:
            mostar_tarefa(x)

def mostar_tarefas_prioridade():
    while True:
        prioridade = input("qual prioridade você dejesa ver: ")
        prioridade = prioridade.lower()
        if prioridade == "alta" or prioridade == "media" or prioridade =="baixa":
            for x in tarefas:
                if x["prioridade"] == prioridade:
                    mostar_tarefa(x)
            break
        else:
            print("opção invalida")

while True:
    print("1 - mostrar todas as tarefas")
    print("2 - mostrar tarefas concluidas")
    print("3 - mostrar tarefas pendentes")
    print("4 - mostrar tarefas por prioridade")
    print("5 - cadastar tarefas nova")
    print("6 - finalizar tarefa")
    print("7 - remover tarefa")
    print("0 - sair")

    opt = input("selecione uma opção: ")
    print("")
    if opt == "1":
        mostrar_todas_tarefas()
    elif opt == "2":
        mostrar_tarefas_concluidas()
    elif opt == "3":
        mostrar_tarefas_pendentes()
    elif opt == "4":
        mostar_tarefas_prioridade()
    elif opt == "5":
        print("criar nova tarefa")
    elif opt == "6":
        print("finalizar tarefa")
    elif opt == "7":
        print("remover tarefa")
    elif opt == "0":
        exit()
    else:
        print("opção invalida")
    print("")