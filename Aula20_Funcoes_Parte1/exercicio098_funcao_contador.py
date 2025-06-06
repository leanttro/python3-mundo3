from time import sleep
def linha():
    print("="*30)

linha()
print(" "*5,"CONTAGEM DE PASSOS")
linha()

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"A contagem de {i} até {f} de {p} em {p} é ")
    sleep(0.5)


    if i < f:
        cont = i
        while cont <= f:
            print(cont,end = " ",flush=True)
            sleep(0.3)
            cont += p
        print("fim") 
    else:
        cont = i
        while cont >= f:
            print(cont,end =" ",flush=True)
            sleep(0.3)
            cont -= p
        print("Fim")       

contador(1,10,1)
linha()
contador(10,0,2)
print("Agora sua vez! Personalize os passos -> ")
i2 = int(input("Início: "))
f2 = int(input("Fim: "))
p2 = int(input("Passo: "))
linha()

contador(i2,f2,p2)
