from time import sleep


def area (l,a):
    are = l * a
    print(f"A área de um terreno {l}x{a} vale {are:.2f}m²")

#Programa Principal 
print(" "*7,"Controle de Terrenos")
print("="*35)
print()
l = float(input("Digite a largura: "))
a = float(input("Digite a altura: "))
sleep(0.5)
area(l,a)
