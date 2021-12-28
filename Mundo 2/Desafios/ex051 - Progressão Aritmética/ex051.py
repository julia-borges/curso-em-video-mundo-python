#Desafio
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

cont = 0

i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
decimo = i + (10 - 1) * p #fórmula do enésimo termo de uma PA

for c in range(i,decimo + p ,p):
    print(f'{c}',end=' → ')
print('ACABOU!')