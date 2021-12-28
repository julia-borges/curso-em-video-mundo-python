#Desafio:
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint

def linha():
    print("-=-" *17)

linha()    
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
linha()    

#entrada
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)

#COMPUTADOR VAI ESCOLHER UM NÚMERO DE 0 Á 5
sorteio = randint(0,5) 

#saída
if sorteio == jogador: 
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {sorteio} e não no {jogador}")