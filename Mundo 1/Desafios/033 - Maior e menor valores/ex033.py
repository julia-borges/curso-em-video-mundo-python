#Desafio
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#entrada
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

#verificando quem é o menor número:
menor =  n1
if n2<n1 and n2<n3:
    menor = n2

if n3<n1 and n3<n2:
    menor= n3

#verificando quem é o maior número:
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

#saída
print("O menor valor digitado foi", menor)
print("O maior valor digitado foi", maior)