lista = []
c = 1
while True:
    n = float(input(f"Digite o valor do {c}º produto: R$"))
    lista.append(n)
    c += 1
    if n > 100:
        print("Atenção! Valor maior que R$100,00. Vai com calma")
    r = int(input("Deseja adicionar outro produto ? NÃO [0] / SIM [1]: "))
    if r not in [0,1]:
        r = int(input("Valor inválido! NÃO [0] / SIM [1]: "))
    if r == 0:
        break
maior = max(lista)
menor = min(lista)
soma = sum(lista)
media = soma / len(lista)

print("="*40)
print(f"O total da compra deu R${soma:.2f}")
print(f"O maior valor da compra foi R${maior} e o menor valor R${menor:.2f}")
print(f"O valor médio da compra foi R${media:.2f}")

"""lista = []
for c in range(1,6):
    n = float(input(f"Digite o valor do {c}º gasto: R$"))
    lista.append(n)
    if n > 100:
        print("Atenção! Produto maior que R$100!")
maior = max(lista)
menor = min(lista)
soma = sum(lista)
media = soma/5

print(f"O maior valor gasto foi: R${maior}")
print(f"O menor valor gasto foi: R${menor}")
print(f"O valor da sua compra foi R${soma}, A média do gasto foi {media}")"""