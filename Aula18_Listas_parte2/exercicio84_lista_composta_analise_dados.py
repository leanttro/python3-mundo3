galera = []
dados = []
c = 0
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pesoatual = dados[1]
    c +=1

    if c == 1:
        maiorpeso = menorpeso = pesoatual
    else:
        if pesoatual > maiorpeso:
            maiorpeso = pesoatual
        if pesoatual < menorpeso:
            menorpeso = pesoatual
    galera.append(dados[:])
    dados.clear()

    e = str(input("Deseja continuar[S/N]: ")).strip().upper()
    if e == "N":
        break
print(f"\nAo todo, você cadastrou {c} pessoas")
print(f"\nO peso maior foi {maiorpeso},  e a pessoa é", end="")
for pessoa in galera:
    if pessoa [1] == maiorpeso:
        print(f"{pessoa[0]}", end = "")
print(f"\nO peso menor foi: {menorpeso}  e a pessoa é", end = "")
for pessoa in galera:
    if pessoa [1] == menorpeso:
        print(f"{pessoa[0]}", end = "")