#Desafio
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#entrada
n = int(input("Me diga um número qualquer: "))

#saída com estrutura composta
if n % 2 == 0:
    print(f"O número {n} é PAR")
else:
    print(f"O número {n} é ÍMPAR")