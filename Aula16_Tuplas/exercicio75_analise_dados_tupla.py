n = 0
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))

l = n1, n2, n3, n4
print(f"Os números digitados foram {l}")
print(f"O número {n1} apareceu {l.count(n1)} vezes")
print(f"O valor {n2} aparece na {l.index(n2)+1}ª posição!")
print("Os números pares são ", end="")
for n in l:
    if n % 2 == 0:
        print(f"{n}", end=" ")

