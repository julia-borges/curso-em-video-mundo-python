#Desafio:
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#importando método shuffle
from random import shuffle

#entrada
n1 = input("Primero aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

#computador escolhe a ordem (aleatório)
lista = [n1, n2, n3, n4]
shuffle(lista)

#saída
print(f"A ordem de apresentação é:")
print(lista)