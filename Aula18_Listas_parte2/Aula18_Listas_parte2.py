galera = []
dados = []
totmaior = totmenor = c = 0
d = 1
while True:
    dados.append(str(input(f"Nome do {d}º inscrito: ")))
    dados.append(int(input(f"Idade do {d}º inscrito: ")))
    galera.append(dados[:])
    dados.clear()
    e = str(input("Deseja continuar[S/N]: ")).strip().upper()
    c = c+1
    d = d+1
    if e == "N":
        break
    
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade \n{"="*30}")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade\n{"="*30}")
        totmenor += 1
print(f"O total de inscritos foram {c}")
print(f"O total de maior de idade é {totmaior} e menor de idade é {totmenor}")


"""galera = []
dado = []
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmenor +=1
print(f"O total de maiores de idade é {totmaior}")
print(f"O total de menores de idade é {totmenor}")

print(galera)

galera = [["Leandro",27],["Michelle", 26], ["Rafaela",40],["Paula",35]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")

teste = []
galera = []
teste.append("Lelis")
teste.append(27)
galera.append(teste[:])
teste[0] = "Ana"
teste[1] = 40
galera.append(teste[:])
print(galera)"""