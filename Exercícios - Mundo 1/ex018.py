#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse Ângulo.

import math

ang = float(input('Ângulo: '))


sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O seno do ângulo {ang}º é {sen:.4f} \nO cosseno é {cos:.4f} \nA tangente é {tan:.4f}.')