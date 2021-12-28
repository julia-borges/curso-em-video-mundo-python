#Desafio
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#entrada
salario = float(input("Salário atual: R$"))

#saída
print(f"Salário com 15% de aumento: R${salario + (salario*15/100):.2f}")