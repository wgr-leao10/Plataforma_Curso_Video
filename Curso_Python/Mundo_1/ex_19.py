from random import choice
print("-=" * 15)
print("Sorteando um Número")
print("-=" * 15)
aluno_1 = str(input("Primeiro Aluno: "))
aluno_2 = str(input("Segundo Aluno: "))
aluno_3 = str(input("Terceiro Aluno: "))
lista_alunos = [aluno_1, aluno_2, aluno_3]
sorteio = choice(lista_alunos)
print(f"O aluno escolhido foi {sorteio}")
print("-=" * 15)
