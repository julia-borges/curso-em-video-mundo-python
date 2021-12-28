#Desafio:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

total_mulher_20 = 0 
homem_mais_velho = 0 
nome_homem_velho = '' 
media = 0

#entrada: vai pedir os dados de 5 pessoas
for p in range(1,5):
    print('-'*15)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    media += idade / 4
    if sexo == 'F':
        if idade < 20:
            total_mulher_20 += 1
    else:
        if p == 1:
            homem_mais_velho = idade
        else:
            if homem_mais_velho < idade:
                homem_mais_velho = idade
                nome_homem_velho = nome            

#saída               
print(f'A média de idade do grupo é: {media} anos')
print(f'O homem mais velho do grupo se chama {nome_homem_velho} e tem {homem_mais_velho} anos')
print(f'Ao todo temos {total_mulher_20} mulheres com menos de 20 anos.')