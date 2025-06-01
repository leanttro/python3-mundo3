from random import randint
from time import sleep
lista = []
jogos = []
print("="*30)
print(f"{" "*5} JOGO DA MEGA SENA {" "*10}")
print("="*30)
quant = int(input("Quantos jogos você quer que eu sorteie: "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("="*30,f"Sorteando {quant} jogos","="*30)
for i,l in enumerate(jogos):
    print(f"Jogos {i+1}: {l}")
    sleep(0.5)
print("*"*5,"Boa Sorte","*"*5)