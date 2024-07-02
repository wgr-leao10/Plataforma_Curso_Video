# dicionário e listas Vazio
pessoas = {}
brasil = []
estado_3 = dict()
brasil_2 = list()
# dicionário Alguns Dados
pessoas_2 = {
    "nome": 'Alice', 'Idade': "25", 'Cidade': "São Paulo"
    }

estado_1 = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado_2 = {'UF': 'São Paulo', "Sigla": 'SP'}
brasil.append(estado_1)
brasil.append(estado_2)
print(brasil[1])

for i in range(0, 3):
    estado_3['Uf'] = str(input('Unidade Federativa: '))
    estado_3['Sigla'] = str(input("Sigla Do estado: "))
    brasil_2.append(estado_3.copy())  # Já no dicionario seria este comando
for j in brasil_2:
    for v in j.values():
        print(v, end=" ")
    print()

# Dicionário dentro de lista
# Acessando Dados
print("O Nome é ", pessoas_2['nome'])
print('A sua Idade', pessoas_2['Idade'])
print(f"O {pessoas_2['nome']} tem {pessoas_2['Idade']} anos")
print(pessoas_2.keys())
print(pessoas_2.values())
print(pessoas_2.items())

# Acessando e Modificando Dados
# Adicionando Um novo Par de Chaves
pessoas_2['Profissão'] = "Engenharia"
print(pessoas_2)
# Modificando Dados
pessoas_2["Idade"] = 26
print(pessoas_2['Idade'])

# Removendo Dados
del pessoas_2['Profissão']
print(pessoas_2)

# Usando Método pop para remover e retornar um valor
# Interando Chaves
for i in pessoas_2.keys():
    print(i)

# Interando Sobre Valores
for j in pessoas_2.values():
    print(j)

# interando sobre Chave e Valor
for i, j in pessoas_2.items():
    print(f'{i}:{j}')
