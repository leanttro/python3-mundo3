lista = []
c = 0
while True:
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar[S/N]: ")).strip().upper()
    lista.append(n)
    c += 1
    if r == "N":
        break
print(f"Você digitou {c} elementos!")
lista.sort(reverse=True)
print(f"Os valores em ordem decressente são {lista}")
if 5 in lista:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")