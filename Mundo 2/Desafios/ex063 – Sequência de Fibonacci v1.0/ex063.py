# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
# Nesse caso, os números seguintes serão a soma dos dois números anteriores, 


print('~'*40)
print('Sequência de Fibonacci')
print('~'*40)

n = int(input('Quantos temos você quer mostrar? '))

#primeiros termos 0 - 1 
penultimo = 0
ultimo = 1   
print('~'*40)
print(f'{penultimo} → {ultimo}', end=' → ')

count = 3
while count <= n:
    termo = ultimo + penultimo # soma dos últimos 2 termos → 0 + 1 = 1
    print(f'{termo}',end=' → ')   
    penultimo = ultimo # transição de termos, penultimo → igual ao ultimo termo = 1
    ultimo = termo    # transição de termos, ultimo → igaul a soma dos dois termos = 1
    count += 1
print('FIM')