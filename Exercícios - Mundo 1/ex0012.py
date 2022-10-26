#Faça um algoritmo que leia o preço do produto e mostra seu novo preço, com 5% de desconto.

p = float(input('Preço: '))
d = 0.95*p

print(f'O preço do produto é {p}, com desconto fica {d:.2f} reais ')