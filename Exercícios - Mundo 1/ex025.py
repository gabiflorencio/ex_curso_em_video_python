#Crie um programa que leia o nome de um pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Digite um nome completo: '))

nome_maior = nome.upper()
resposta = 'SILVA' in nome_maior
print(f'O nome possui SILVA? {resposta}')