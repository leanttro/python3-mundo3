palavras = "aprender", "programar", "linguagem", "python", "aprender", "curso", "gratis", "ensino", "qualidade"
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ", end = "")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"{letra}",end=" ")
            