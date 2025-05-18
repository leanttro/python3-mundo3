lista = [[],[]]
valor = 0
for c in range (1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor %2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print("="*40)
lista[0].sort()
print(f"Os números pares são {lista[0]}")
lista[1].sort()
print(f"Os números ímpares são {lista[1]}")