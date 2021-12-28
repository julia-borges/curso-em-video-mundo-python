#Desafio
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

#entrada
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

#saída
print(f'Quem tirou {nota1} e {nota2} tem a média {media:.2f}')
if media < 5.0: 
    print('O aluno está REPROVADO!')
elif media > 5.0 and media < 6.9:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7.0:
    print('O aluno está APROVADO!')