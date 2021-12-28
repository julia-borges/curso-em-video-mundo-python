#Desafio:
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

#entrada
velocidade = float(input("Qual é a velocidade atual do carro? "))

#saída com condição
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f"MULTADO! Você excedeu o limite permitido que é o de 80Km/h")
    print(f"Você deve pagar uma multa de R$ {multa:.2f}!")
print("Tenha um bom dia! Dirija com segurança!")