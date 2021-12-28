#Desafio
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#entrada
distancia = float(input("Qual é a distância da sua viagem? "))

#estrutura condicional composta
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

#saída
print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
print(f"E o preço da sua passagem será de R${valor:.2f}")