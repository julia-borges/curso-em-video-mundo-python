#Desafio
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#entrada
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg*alt

#saída
print(f"Considerando a dimensão de {larg}x{alt} a sua área é de {area}m")
print(f"Para pintar essa parede, você precisará de {area/2}l de tinta")