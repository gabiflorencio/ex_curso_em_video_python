'''
Faça um programa que leia uma frase pelo teclado e mostre:

    Quantas vezes aparece a letra 'A'

    Em que posição ela aparece a primeira vez.

    Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: '))

frase_maior = frase.upper()

quant_letra = frase_maior.count('A') #Quantas vezes a letra A aparece
frase_prim = frase_maior.find('A') #Em que posição ela aparece a primeira vez

frase_fim = frase_maior.find('A', ),


 