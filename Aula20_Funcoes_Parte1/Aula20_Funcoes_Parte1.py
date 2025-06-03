def soma (*valores):
    som = 0
    for num in valores:
        som += num
    print(f"Somando os valores {valores} temos {som}")

soma(2,5)
soma(9,15,235,14)
soma(5,4,85)


"""def dobra (lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [0,15,24,14,235,35,1]
print(valores)
dobra(valores)
print(valores)"""




"""def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e a quantidade é {tam}")



contador(1,2)
contador(4,5,6)
contador(5,6,7,8,9)




def contador(*num):
    for valor in num:
        print(valor, end=" ")
    print("Fim")



contador(1,2)
contador(4,5,6)
contador(5,6,7,8,9)



def soma(a,b):
    print(f"A = {a} B = {b}")
    s = a + b
    print(f"A soma de {a} + {b} é {s}")


a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
soma(a,b)
soma(b = 5,a = 6)"""

"""def titulo (txt):
    print("="*30)
    print(txt)
    print("="*30)

titulo("Conversor de Moedas")
n = input("Digite um valor: ")


titulo("RESULTADO")
print(n)"""


"""def lin():
    print("="*30)

lin()
print(" "*6,"CONVERSOR DE MEDIDAS")
lin()
lin()"""