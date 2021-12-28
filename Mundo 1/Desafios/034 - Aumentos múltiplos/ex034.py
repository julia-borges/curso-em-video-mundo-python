#Desafio
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#entrada
salario = float(input("Qual é o salário do funcionário? R$"))

#condição composta
if salario > 1250.00:
    novo = (salario*0.10) + salario
else:
    novo = (salario*0.15) + salario

#saída
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.")