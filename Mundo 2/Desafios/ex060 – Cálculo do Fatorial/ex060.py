# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1

print(f"Calculando {n}! =",end=" ")
while c > 0:
    print(f"{c}", end=" ")
    print("x" if c > 1 else "=",end=" ") #é possível colocar if no print
    f*=c
    c-=1 
print(f)