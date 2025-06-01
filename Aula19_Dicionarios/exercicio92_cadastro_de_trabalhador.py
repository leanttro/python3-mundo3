cadastro = {}
cadastro["Nome"] = str(input("Nome: "))
anonasc = int(input("Ano de Nascimento: "))
idade = 2025 - anonasc
cadastro["Idade"] = idade
cadastro["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro["CTPS"] == 0:
    for k, v in cadastro.items():
        print("="*40)
        print(f"- {k} tem o valor {v}")
else:
    cadastro["Contratação"] = int(input("Ano de Contratação: "))
    cadastro["Salário"] = float(input("Salário: "))
    print()
    ano1 = 35 - (2025 - cadastro["Contratação"]) 
    cadastro["Aposentadoria"] = idadeaposent = idade + ano1
    for k, v in cadastro.items():
        print(f"- {k} tem o valor de {v}")
        print("="*50)
     