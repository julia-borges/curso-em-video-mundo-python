#Desafio:
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#importando método choice
from random import choice

#entrada
nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")

#computador escolhe um nome aleatório
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista) 

#saida
print(f"O nome escolhido foi {sorteio}")