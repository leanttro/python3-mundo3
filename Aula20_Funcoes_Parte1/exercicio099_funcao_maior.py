

print(f"Analisando os valores passados: ")

nummaior = 0
def maior (*num):
    lista = []
    cont = nummaior = 0
    print()
    print(f"Os valores são", end = " ")
    for k in num:
        print(k, end = " ")
        cont +=1
        lista.append(k)
        nummaior = max(lista)


maior(7,5,4,6,4)
maior(4,5,8,5)
maior(1,2)

nummaior = max(lista)
print(nummaior)