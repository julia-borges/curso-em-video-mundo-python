#Desafio:
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#entrada
var = input("Digite algo: ")

#saída
print(f"O tipo primitivo desse valor é: {type(var)}")
print(f"Só tem espaços? {var.isspace()}")
print(f"É um número? {var.isnumeric()}")
print(f"É alfabético? {var.isalpha()}")
print(f"É alfanuumérico? {var.isalnum()}")
print(f"Está em maiúscula? {var.isupper()}")
print(f"Está em minúscula? {var.islower()}")
print(f"Está capitalizada? {var.istitle()}") 
