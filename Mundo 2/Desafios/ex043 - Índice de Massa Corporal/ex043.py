#Desafio
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

#entrada
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

#saída
print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está na faixa de PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está em Obesidade!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')