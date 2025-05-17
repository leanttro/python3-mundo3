maior = 0
menor = 0
list = []
for c in range(0,5):
        list.append(int(input(f"Digite um valor para posição {c}: ")))
        if c == 0:
                maior = menor = list[c]
        else:
            if list[c] > maior:
                   maior = list[c]
            if list[c] < menor:
                   menor = list[c]
print(list)
print(f"O maior valor digitado foi {maior} nas posições: ", end ="")
for i, v in enumerate(list):
    if v == maior:
        print(f"{i}...", end ="")    
print()
print(f"O menor número {menor} e está nas posições: ", end = "")
for i, v in enumerate(list):
    if v == menor:
        print(f"{i}...", end ="")
print()


"""valores = list()
for cont in range(0,5):
    valores.append(int(input(f"Digite um valor para posição {cont}: ")))
maior = max(valores)
menor = min(valores)
print(f"Você digitou os valores: {valores}")
print(f"O maior valor foi: {maior}, na posição {valores.index(maior)} ")
print(f"O menor valor foi: {menor}, na posição {valores.index(menor)}")"""
