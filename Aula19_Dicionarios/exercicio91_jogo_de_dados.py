from random import randint
from time import sleep
from operator import itemgetter
print("="*30)
print(" "*6,"JOGO DE DADO")
print("="*30)
sleep(0.5)
print()
jogo = {"Jogador1": randint(1,6), 
        "Jogador2": randint(1,6),
        "Jogador3": randint(1,6),
        "Jogador4": randint(1,6)}
ranking = ()
print("Valores Sorteados")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.4)
print()
print("="*30)
print(" "*9,"RANKING")
print("="*30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}.")
    sleep(0.5)


"""from random import randint
from time import sleep
from operator import itemgetter
dic = {}
lista = []
print("="*30)
print(" "*6,"JOGO DE DADO")
print("="*30)
sleep(0.5)
print(" "*6,"Sorteando...")
print()
sleep(1)
ranking = []
for c in range(0,4):
    dic['Numero Sorteado'] = randint(1,6)
    ranking.append(dic)
    c = c + 1
    for v in dic.values():
        print(f"Jogador{c} tirou {v} no dado")
        sleep(0.5)
    ranking = sorted(dic.items(),key=itemgetter(1), reverse=True)
print(ranking)"""
