#Desafio:
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip()

a = frase.upper().count("A")
primeiro = frase.upper().find("A") + 1
ultima = frase.upper().rfind("A") + 1


print(f"Sua frase contem {a} letras A ")
print(f"A posição da primeira letra A é: {primeiro}")
print(f"A posição da sua última letra A é: {ultima} ")