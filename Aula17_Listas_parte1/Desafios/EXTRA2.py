print("="*45)
print(f"{" "*10}Gerenciador de tarefas{" "*10}")
print("="*45)
lista = []
while True:
    print(" [1] - Adicionar Tarefa")
    print(" [2] - Excluir Tarefa")
    print(" [3] - Mostrar Lista")
    print(" [0] - Encerrar")
    r = int(input("Número de escolha: "))
    if r == 1:
        while True:
            n = str(input("Digite uma tarefa PARA ADICIONAR: "))
            lista.append(n)
            lista.sort()
            print("Tarefa adicionada com sucesso!")
            print("[0] - Adicionar mais um item ")
            print("[1] - Voltar ao Menu")
            
            e = str(input("Escolha: "))
            while e not in ["0","1"]:
                print("Valor inválido!")
                e = str(input("Digite novamente: "))

            if e == "1":
                break
    elif r == 2:
        n = str(input("Digita uma tarefa PARA EXCLUIR: "))
        lista.remove(n)
        lista.sort()
        print("Tarefa excluída com sucesso! ")
    elif r == 3:
        print(f"{"LISTA"}")
        for i, listaformatada in enumerate(lista,1):
            print(f"{i}. {listaformatada}")
    elif r == 0:
         break
    else:
        print("Número inválido, Tente novamente")
