#Desafio:
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#entrada
reais = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = 3.27

conversao = reais / dolar

#saída
print(f"Com R${reais} reais você pode comprar US${conversao:.2f} dolares")