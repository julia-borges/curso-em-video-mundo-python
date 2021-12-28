#Desafio:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# - importando método p calcular hipotenusa
from math import hypot

#entrada
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hi = hypot(co, ca)

#saída
print(f"A hipotenusa vai medir: {hi:.2f}")


## Resolução na matemática sem importação
# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("Comprimento do cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2) 
# print(f"A hipotenusa vai medir {hi:.2f}")