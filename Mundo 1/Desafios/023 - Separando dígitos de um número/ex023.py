#Desafio:
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#entrada:
num = int(input("Digite um número: "))

#conversão do número para unidade, dezena, centena e milhar
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#saída
print(f"unidade:{u}")
print(f"dezena:{d}")
print(f"centena:{c}")
print(f"milhar:{m}")