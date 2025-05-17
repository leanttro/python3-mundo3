n = str(input("Digite a expressão: "))
pilha = []

for simbolo in n:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("A expressão está correta")
else:
    print("A expressão está incorreta")