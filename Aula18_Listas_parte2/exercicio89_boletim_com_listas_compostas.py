ficha = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resposta = str(input("Quer continuar [S/N]: ")).upper()
    if resposta == "N":
        break
print("=*"*40)
print(f"{"N°":<4}{"Nome":<8}{"Média":>10}")
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<8}{a[2]:<10}")
while True:
    print("=*"*40)
    opc = int(input("Mostrar notas de qual aluno [999 para encerrar]: "))
    if opc == 999:
        print("FINALIZADO...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<<Volte sempre>>>")