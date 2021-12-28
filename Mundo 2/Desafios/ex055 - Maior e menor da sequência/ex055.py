#Desafio
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f'O maior peso lido foi {maior}kg.')
print(f'O menor peso lido foi {menor}kg.')