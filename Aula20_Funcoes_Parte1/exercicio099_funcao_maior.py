def maior (*num):
    cont = maior = 0
    print("\nAnalisando os valores")
    for valor in num:
        print(f"{valor}",end =" ")
        if valor == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
            cont +=1
    print(f"Foram informados {cont} valores")
    print(f"O maior valor informado foi {maior}")



maior(7,5,4,6,4)

maior(4,5,8,5)

maior(1,2)

maior(6)

maior()
