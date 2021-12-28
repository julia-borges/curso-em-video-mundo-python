#Desafio:
#Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

#entrada
nome = str(input("Nome completo: ")).strip()

#tira o espaço da frase
sem_espaço = nome.replace(' ', '') 

#saída
print(f"Seu nome em maiúsculo é: {nome.upper()}")
print(f"Seu nome em minúsculo é: {nome.lower()}")
print(f"Seu nome tem ao todo: {len(sem_espaço)} letras")      
print(f"Seu primeiro nome tem: {nome.find(' ')} letras")