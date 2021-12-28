#Desafio:
#Crie um programa que faça o computador jogar Jokenpô com você.

#importando funções para usar no jogo
from random import randint
from time import sleep

#computador joga
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)           #computador escolhe uma posição aleatória entre 0 e 2

print('''Escolha:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

#usuário joga
jogador = int(input('Sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

#saída das respostas de ambos os jogadores
print('-='*13)
print(f'Você jogou : {itens[(jogador)]}')
print(f'Computador jogou: {itens[(computador)]}')
print('-='*13)

#saída do vencedor
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('DEU EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('DEU EMPATE!!!')