#Desafio
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#importando metodo date para pegar o ano atual da máquina
from datetime import date

#entrada
ano = int(input("Que ano quer analisar? Coloque 0 para anaisar o ano atual: "))

#saída com condição
if ano == 0:
    ano = date.today().year 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")