nota_1 = float(input('Primeira Nota: '))
nota_2 = float(input('Segunda Nota: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print(f'Tirando {nota_1} e {nota_2} a média do aluno é {media} o aluno está REPROVADO')
elif media >= 5 and media <= 6.9: # pode ser assim 7 > media >=5
    print(f'Tirando {nota_1} e {nota_2} a média do aluno é {media} o aluno está em RECUPERAÇÃO')
elif media >= 7:
    print(f'Tirando {nota_1} e {nota_2} a média do aluno é {media} o aluno está APROVADO')
