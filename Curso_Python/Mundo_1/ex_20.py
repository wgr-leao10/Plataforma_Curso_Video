from random import shuffle
print("-=" * 15)
print("Sorteando De Alunos")
print("-=" * 15)
aluno_1 = str(input("Primeiro Aluno: "))
aluno_2 = str(input("Segundo Aluno: "))
aluno_3 = str(input("Terceiro Aluno: "))
aluno_4 = str(input("Quarto Aluno: "))
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
ordem_de_apresentacao = shuffle(lista_alunos)
print(f"A ordem de apresentação será {ordem_de_apresentacao}")
print("-=" * 15)
