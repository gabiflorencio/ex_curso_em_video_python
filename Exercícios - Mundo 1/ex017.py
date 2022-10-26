#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

h = math.hypot(co, ca)

print(f'A hipotenusa desse triângulo será: {h:.3f}.')
