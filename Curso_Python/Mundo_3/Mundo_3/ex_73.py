print("-=" * 25)
print("Tabela do Brasileirao")
print("-=" * 25)
times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo"
         "Vasco", "Chapocoense", "Atlético", "Botafogo", "Atletico -PR",
         "Bahia", "São Paulo", 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print("Lista de Times: ", times)
print('Os 5 Primeiros Times Colocados:', times[0:5])
print("Os 4 ùltimos times Colocados:", times[15:])
print("Os Times em Ordem Alfabética:", sorted(times))
print("A Posição do Chapocoense:", times.index("Chapocoense") + 1)
