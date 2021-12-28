#Desafio
#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

sorteio = randint(0, 10)

print('Acabei de pensar em um número 🤔. .')
jogador = int(input('Você é capaz de adivinhar ?... '))

c = 0
while jogador != sorteio:
    if  jogador < sorteio :
        print('Mais... Tente mais uma vez.')
        jogador = int(input('Qual seu palpite ? '))
    else:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual seu palpite ? '))
    c+=1

print('-' * 36)
print(f'Acertou! Com {c} tentativas. Parabéns!🥳')
print('-' * 36)