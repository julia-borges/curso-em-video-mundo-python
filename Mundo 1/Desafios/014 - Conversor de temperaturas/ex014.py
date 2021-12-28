#Desafio:
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

#entrada
c = float(input("Informe a temperatura em °C: "))

#cálculo
conversao = 9 * c / 5 + 32

#saída
print(f"A temperatua de {c}°C corresponde a {conversao}°F!")