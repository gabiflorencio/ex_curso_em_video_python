#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Largura: '))
a = float(input('Altura: '))
area = l * a

print(f'Para pintar a área de {a}m², será necessário {a/2} litro(s) de tinta. ')