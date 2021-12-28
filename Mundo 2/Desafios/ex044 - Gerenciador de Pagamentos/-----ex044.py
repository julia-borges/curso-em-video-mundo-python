#Desafio
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print('=-=-=-=-= LOJA JUJUBA =-=-=-=-=')

preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')

opcao = int(input('Qual é a opção? '))
if opcao == 1:                         #opção com desconto de 10%  
    total = preço - (preço * 10 / 100)
elif opcao == 2:                       #opção com desconto de 5% 
    total = preço - (preço * 5 / 100) 
elif opcao == 3:                       #opção s/ desconto parcelado 2x
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS!')
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcela em {total_parcelas}x de R${parcela:.2f} COM JUROS!')
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')