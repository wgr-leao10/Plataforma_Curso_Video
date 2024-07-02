teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # no amterial da matéria a um relatório detalhado
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # Este comando é importante
galera.append(teste[:])  # Este comando é importante pois aqui ele faz a cópia
print(galera)
