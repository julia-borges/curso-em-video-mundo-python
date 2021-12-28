#Desafio:
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

#entrada
preco = float(input("Qual é o preço do produto? R$"))

#saída
print(f"Valor total com desconto de 5% é: R$ {preco - (preco * 5 / 100):.2f}") # ou {preco -(preco*0.05)}