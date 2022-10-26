'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

    O nome com todas as letras maiúsculas
    O nome com todas minúsculas.
    Quantas letras ao todo (sem considerar espaços).
    Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: '))
maior = nome.upper()
menor = nome.lower()
letras = len(nome) - nome.count(' ')
primeiro = nome.split()
print(f'Nome em maiúsculo: {maior} \n Nome em minúsculo: {menor} \n O nome possui {letras} letras\n O primeiro nome é: {primeiro[0]}')