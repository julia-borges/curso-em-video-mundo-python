#Desafio:
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#entrada
nome = input("Qual é o seu nome? ").strip()

procura = "SILVA" in nome.upper()

#saída
print(f"Seu nome contém Silva? {procura}")