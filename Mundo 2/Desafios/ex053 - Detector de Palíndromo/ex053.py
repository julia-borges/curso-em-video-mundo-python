#Desafio:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# EXEMPLOS: 
# [ APOS A SOPA ], [A SACADA DA CASA], [A TORRE DA DERROTA], [O LOBO AMA O BOLO], [ANOTARAM A DATA DA MARATONA].

#.replace(' ', '') >> tira espaço, mas ñ dá p usar nesse programa

frase = input('Digite uma frase: ').strip().upper()
l = frase.split()      #para gerar uma lista
junto = ''.join(l)     #juntei a lista p eliminar os espaços antes/depois
inverso = ''           #inverte

for l in range(len(junto)-1,-1,-1): #dá última letra até a primeira voltando 1 letra
    inverso += junto[l]
print(f'O inverso de {junto} é: {inverso}')
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')


''' 
Outro jeito:

frase = input('Digite uma frase: ').strip().upper()
l = frase.split()
junto = ''.join(l)
inverso = junto[::-1]

print(f'O inverso de {junto} é: {inverso}')

if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
'''