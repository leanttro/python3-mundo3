from random import randint

def sorteia(numeros):
    for cont in range(0,5):
        numeros .append(randint(1,10))

def somapar(numeros):
    soma = 0
    for v in numeros:
        if v % 2 ==0:
            soma+= v
    print(f"Somando os valores PARES de {numeros} temos {soma}")


numeros = list()
sorteia(numeros)
print(numeros)
somapar(numeros)