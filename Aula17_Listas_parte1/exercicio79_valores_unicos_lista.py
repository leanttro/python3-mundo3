num = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar! ")
    resposta = str(input("Quer Continuar [S/N]: "))
    if resposta in "Nn":
        break
num.sort()
print(f"Você digitou os valores {num}")