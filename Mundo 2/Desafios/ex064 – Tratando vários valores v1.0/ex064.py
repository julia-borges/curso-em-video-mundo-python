#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = contador = acumulador = 0
n = int(input('Digite um número [999 para parar]: '))

while n != 999:
        contador+=1
        acumulador += n
        n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {acumulador}.')   