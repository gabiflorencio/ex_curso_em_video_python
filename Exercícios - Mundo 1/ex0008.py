#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))
c = n*100
m = n*1000

print(f'O valor {n}m possui {c}cm e {m}mm.')