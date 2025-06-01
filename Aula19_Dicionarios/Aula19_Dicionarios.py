estado = {}
brasil = []
for c in range(0,3):
    estado['UF'] = str(input("Unidade Federativa: "))
    estado['Sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end=" ")
    print()
    
    """
estado = {}
brasil = []
for c in range(0,3):
    estado['UF'] = str(input("Unidade Federativa: "))
    estado['Sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f"{k} = {v}", end = " ")
    print()"""


"""brasil = []
estado1 = {"Uf":"São Paulo","Sigla": "SP" }
estado2 = {"Uf":"Rio de Janeiro","Sigla":"RJ"}
estado3 = {"Uf":"Bahia","Sigla":"BA"}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil[1]['Sigla'])
print(brasil[0]['Uf'])"""


"""pessoas = {"Nome": "Leandro","Idade": 27,"Sexo":"M"}
print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos e é do sexo {pessoas['Sexo']}")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']
pessoas['Nome'] = "Gustavo"
pessoas['Peso'] = 82
for k, v in pessoas.items():
    print(f"{k} = {v}")"""
