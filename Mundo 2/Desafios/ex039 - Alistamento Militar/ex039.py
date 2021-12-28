#Desafio:
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#importa a data atual da máquina
from datetime import date

#entrada
nascimento = int(input('Ano de nascimento: '))

ano = date.today().year
idade = int(ano - nascimento)

#saída
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')
if idade == 18:
    print('Já está na hora de se alistar! Faça isso entre 01 janeiro e 30 de junho!')
elif idade > 18:
    print(f'Você deveria ter se alistado a {idade-18} anos')
    print(f'Seu alistamento foi em {ano - (idade-18)}')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento')
    print(f'Seu alistamento será em {ano + (18 - idade)}')