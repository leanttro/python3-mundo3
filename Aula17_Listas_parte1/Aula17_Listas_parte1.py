a = [1,2,5,4,48,56]
b = a[:]
b[4] = 15
print(f"Lista A {a}")
print(f"Lista B {b}")

"""valores = list ()
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))
print(valores)

valores = list()
valores.append(9)
valores.append(15)
valores.append(12)

for cont, v in enumerate(valores):
    print(f"Na posição {cont} encontrei o valor {v}")

for v in valores:
    print(f" {v}...", end=" ")
print("\nCheguei ao final da lista")

num = [2,5,9,1]
num[3] = 8
num.insert(0,6)
num.append(15)
num.sort(reverse=True)
num.sort()
num.pop(1)
num.insert(1,2)
if 15 in num:
    num.remove(15)
else:
    print("Não achei o número")
for cont in range (0, len(num)):
    print(num[cont], end=" ")"""