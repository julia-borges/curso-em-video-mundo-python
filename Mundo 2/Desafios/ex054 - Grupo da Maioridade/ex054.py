#Desafio
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano = date.today().year 
maior = 0
menor = 0

for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')