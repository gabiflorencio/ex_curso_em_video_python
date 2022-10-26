#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Salário: '))
a = s*1.15

print(f'Seu salário era {s} reais, com o novo aumento ele ficou {a:.2f} reais')