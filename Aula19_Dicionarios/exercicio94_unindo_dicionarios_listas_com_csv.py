import csv

dados = {}
cadastro = []
opc = 0
c = 0
total = 0
mulheres = 0
while True:
    dados['Nome'] = str(input("Nome: "))
    while True:
        dados['Sexo'] = str(input("Sexo[F/M]: ")).upper()
        if dados["Sexo"] not in "FfMm":
            print("Erro! Digite F ou M, por favor")
        else:
            break            
    dados['Idade'] = int(input("Idade: "))
    cadastro.append(dados.copy())
    c += 1
    total += dados['Idade']
    while True:
        opc = str(input("Deseja continuar [S/N]: ")).upper()
        if opc in "SsNn":
            break
        else:
            print("Erro! Digite S ou N, por favor")
    if opc in "Nn":
        break
media = total/c

with open("cadastro.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    campos = ["Nome", "Sexo", "Idade"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    for pessoa in cadastro:
        escritor.writerow(pessoa)

print("="*30)
print(f"A) Ao todo você cadastrou {c} pessoas")
print(f"B) A média de idades é {media:.2f}")
print("C) As mulheres cadastradas são: ")
for pessoa in cadastro:
    if pessoa["Sexo"] == "F":
        print(f"   -> {pessoa['Nome']}")
print("D) As pessoas com idade acima da média: ")
for pessoa in cadastro:
    if pessoa["Idade"] > media:
        for k,v in pessoa.items():
            print(f"{k} = {v}", end=" ")
        print()
print("Encerrando...")