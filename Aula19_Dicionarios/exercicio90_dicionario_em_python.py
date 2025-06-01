aluno = {}
boletim = []
print("="*30)
while True:
    aluno["Nome"] = str(input("Nome: "))
    aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))
    print("="*30)
    if aluno['Média'] > 7:
        aluno["Situação"] = "Aprovado"
    elif aluno['Média'] < 5:
        aluno['Situação'] = "Reprovado"
    else:
        aluno["Situação"] = "Recuperação"
    boletim.append(aluno.copy())
    for b in boletim:
        for k, v in b.items():
            print(f"{k} = {v}")
    print("="*30)
    opc = str(input("Deseja continuar [S/N]: ")).upper()
    if opc in "Nn":
            break

