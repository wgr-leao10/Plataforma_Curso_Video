soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
menor_que_20_mulher = 0
for i in range(1, 5):
    print("-----{}° Pessoa----".format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma_idade += idade
    media_idade = soma_idade / 4
    if i == 1 and sexo in 'Mn':
        maior_idade_homem = idade
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        menor_que_20_mulher += 1
print(f"A media de Idade do Grupo é {media_idade}")
print(f"O homem Mais Velho tem {maior_idade_homem} e chama {nome_mais_velho}")
print(f"A o todo são {menor_que_20_mulher} mulheres com menos de 20 anos")
