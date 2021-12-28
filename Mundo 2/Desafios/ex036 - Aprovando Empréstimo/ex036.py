#Desafio: 
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#entrada
valor = int(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Quantos anos pretende pagar? "))

prestacao = (valor / anos) / 12
minimo = salario * 0.30

#saída
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacao))

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')