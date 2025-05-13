listagem = "Borracha", 2, "Lápis", 1.85, "Caderno", 18.95, "Apontador", 0.99, "Mochila", 152, "Lapiseira", 14
print("*"*40)
print(f"{"LISTA DE MATERIAIS":^40}")
print("*"*40)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f"{listagem[posicao] :.<30}R$",end = "")
    else:
        print(f"{listagem[posicao]:>7.2f}")
print("*"*40)