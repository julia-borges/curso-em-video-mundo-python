#Desafio
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

#entrada
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

#saída
if a < b + c and b < c + a and c < b + a:
    print('Os segmentos acima PODEM FORMAR triângulo', end=' ')
    if a == b and b == c:
         print('EQUILÁTERO!')
    elif a != b and b != c and c != a :
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')        
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')