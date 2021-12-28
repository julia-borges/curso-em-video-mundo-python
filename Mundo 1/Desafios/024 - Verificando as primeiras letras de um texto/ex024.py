#Desafio
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Em que cidade você mora? ")).strip() #tira os espaços

#verifica se a cidade digitada (posição 0 a 4) é igual a "SANTO"
print(cidade[:5].upper() == "SANTO")