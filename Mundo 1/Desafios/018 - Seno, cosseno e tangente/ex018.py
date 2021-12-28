#Desafio:
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

#entrada
a = int(input("Digite o ângulo que você deseja: "))

#cálculos 
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

#saída
print(f"O ângulo de {a} tem o SENO de {seno:.2f}")
print(f"O ânuglo de {a} tem o COSSENO de {cos:.2f}")
print(f"O ângulo de {a} tem a TANGENTE de {tan:.2f}")