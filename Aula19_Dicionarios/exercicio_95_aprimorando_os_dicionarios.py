jogador = {}
quantgol = []
jogador["Nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas o {jogador['Nome']} jogou? "))
for c in range(partidas):
    gols = int(input(f"     Quantos gols na partida {c+1} ? "))
    quantgol.append(gols)
jogador["Gols"] = quantgol[:]
jogador["Total"] = sum(quantgol)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas")
for i, c in enumerate(jogador["Gols"]):
    print(f"      ==> Na partida {i+1}, fez {c} gols")
print(f"Foi um total de {sum(quantgol)} gols.")