times = "Palmeiras", "Flamengo", "Bragantino", "Cruzeiro", "Fluminense", "Atlético-MG", "Bahia", "Botafogo", "Ceará SC", "Corinthians", "Fortaleza", "Mirassol", "Internacional", "EC Vitória", "Grêmio", "São Paulo", "Vasco da Gama", "Juventude", "Santos", "Sport Recife"
print(f"Lista de times - > {times}")
#for t in times:
    #print(t)
print("="*90)
print(f"Os 5 primeiros são {times[0:5]}")
print("="*90)
print(f"Os últimos 4 colocados são {times[-4:]}")
print("="*90)
print(sorted(times))
print("="*90)
print(f"O cruzeiro está na posição está {times.index("Cruzeiro")+1}")
