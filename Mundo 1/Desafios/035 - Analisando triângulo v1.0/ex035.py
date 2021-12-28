#Desafio
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#função para o print
def linha():
    print("-=-"*11)

linha()
print("Analisador de Triângulos")
linha()

#entrada
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

#saída com condição composta
if a < b + c and b < c + a and c < b + a:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")