lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = str(input("Quer continuar [S/N]: ")).strip().upper()
    if r == "N":
        break
for i,v in enumerate(lista):
    if v %2 == 0:
        pares.append(v)
    if v%2 == 1:
        impares.append(v)
lista.sort()
print(f"A lista completa em ordem crescente é {lista}")
pares.sort()
print(f"A lista de pares é {pares}")
impares.sort()
print(f"A lista de ímpares é {impares}")
