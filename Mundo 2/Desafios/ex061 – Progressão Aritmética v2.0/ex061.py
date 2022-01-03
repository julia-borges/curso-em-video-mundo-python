# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input("Qual o primeiro termo: "))
razao = int(input("Qual a razão: "))
c = 1
termo = primeiro

while c <= 10:
    print(f"{termo}", end=' → ')
    termo+= razao
    c+=1
print("FIM")