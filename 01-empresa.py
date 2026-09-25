clientes = [
    {"nome":"Ana","cel":"11988887777", "empresa":"FIAT"},
    {"nome":"Pedro","cel":"11988886666", "empresa":"INTEL"},
    {"nome":"Maria","cel":"119888855555", "empresa":"SEBRAE"},
    {"nome":"Felipe","cel":"11988884444", "empresa":"INTEL"}
]

#pocura um cliente por meio do nome da empresa
def cliente_por_empresa():
    empresa = input("digite a empresa: ")
    for cliente in clientes:
        if cliente["empresa"] == empresa.upper():
            print(cliente)

#cadastra um novo cliente
def cadastrar_cliente():
    nome = input("digite o nome do cliente: ")
    cel = input("digite o celular do cliente: ")
    empresa = input("digite a empresa do cliente: ")

    clientes.append({"nome":nome,"cel":cel, "empresa":empresa.upper()})

#remove o cliente da lista
def remover_cliente():
    cliente_r = input("digite o nome do cliente a ser deletado: ")
    index = 0
    ultimo = len(clientes)-1
    while index <= ultimo:
        if clientes[index]["nome"].lower() == cliente_r.lower():
            clientes.pop(index)
            break
        index +=1
    

while True:
    print("1 - cadastrar cliente")
    print("2 - procurar cleinte pela empresa")
    print("3 - remover cliente")
    print("0 - sair")
    print("")
    opt = input("digite uma opção: ")

    if opt == "1":
        print("")
        cadastrar_cliente()
        print("")
    elif opt == "2":
        print("")
        cliente_por_empresa()
        print("")
    elif opt == "3":
        print("")
        remover_cliente()
        print("")
    elif opt == "0":
        exit()
    else:
        print("opção invalida")


