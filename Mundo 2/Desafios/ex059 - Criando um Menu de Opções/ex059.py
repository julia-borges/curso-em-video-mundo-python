# Desafio:
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 1

while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa '''  )
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao == 1:
         print(f'{primeiro} + {segundo} é igual a {primeiro + segundo}')
    elif opcao == 2:
        print(f'{primeiro} x {segundo} é igual a: {primeiro*segundo}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'Entre {primeiro} e {segundo} o maior valor é {primeiro}')
        else:
            print(f'Entre {primeiro} e {segundo} o maior valor é {segundo}')  
    elif opcao == 4:
        print('Informe os novos números: ')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: ')) 
    elif opcao > 5: 
        print('Opção inválida. Tente novamente')
    print('-=='*8)
    sleep(2)
print('Finalizando. . .')
sleep(1)
print('-=='*8)
print('Fim do programa, volte sempre!!')