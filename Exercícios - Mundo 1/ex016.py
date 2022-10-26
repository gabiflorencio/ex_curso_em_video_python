#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

n = float(input('Digite um número: '))

t = math.trunc(n)

print (f'A porção inteira do número é {t}')