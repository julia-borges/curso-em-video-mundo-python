#Desafio
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split() #dividir em espaços, manda para uma lista

print("Muito prazer em te conhecer")
print("Seu primeiro nome é", nome[0])
print("Seu último nome é", (nome[len(nome)-1]))