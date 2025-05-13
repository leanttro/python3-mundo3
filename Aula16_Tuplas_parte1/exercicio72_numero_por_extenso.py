n = int(input("Digite um número: "))
while n not in range(0,21):
    n = int(input("Tente novamente. Digite um número: "))
num = "zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
print(f"Você digitou o número {num[n]}")